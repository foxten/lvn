from lvn_app.config import Config
from pianosdk import Client
from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import json
import sys
import time
import base64
import re

PIANO_CLIENT = Client(api_host=Config.PIANO_HOST, api_token=Config.PIANO_API_TOKEN,
                      private_key=Config.PIANO_PRIVATE_KEY)


def add_mvault_and_token_to_piano_user(mvault_id: str, token: str, user): #ignoring
    """
    Takes the Mvault ID and Token String returned from the Mvault API and
    saves them on the User record in Piano.
    Note: The feature to update custom fields from the Piano python SDK wasn't working,
    so we're contacting the API directly here.
    """
    resp = requests.post(
        url=Config.PIANO_API_URL
            + "/publisher/user/update?aid="
            + Config.PIANO_APP_ID
            + "&api_token=" + Config.PIANO_API_TOKEN + "&uid=" + user.uid,
        headers={'Content-type': 'application/json'},
        auth=(Config.MVAULT_KEY, Config.MVAULT_SECRET),
        data=json.dumps({"passport-auth": token, "mvault_id": mvault_id})
    )
    if resp.ok:
        print('Successfully added passport auth token ' + token + ' to user ' + user.uid + ' in piano')
    else:
        print('Could not add passport auth token ' + token + ' to user ' + user.uid + ' in piano')
        print(resp.content, file=sys.stderr)

    # Add activation token to campaign monitor custom fields
    if Config.CAMPAIGN_MONITOR_API_URL:
        for list_id in Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST.split(','):
            resp = requests.put(
                url=Config.CAMPAIGN_MONITOR_API_URL + "/subscribers/" + list_id + ".json",
                params={'email': user.email},
                headers={'Content-type': 'application/json'},
                auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
                data=json.dumps({
                    "CustomFields": [{"Key": "passport-auth", "Value": token}],
                    "ConsentToTrack": "Unchanged",
                })
            )
            if resp.ok:
                print('Successfully added passport auth token ' + token + ' to user ' + user.uid + ' in campaign monitor')
            else:
                print('Could not add passport auth token ' + token + ' to user ' + user.uid + ' in campaign monitor')
                print(resp.content, file=sys.stderr)


def register_user_on_pbs(user_id: str, register_data): #ignoring
    """
    Takes the user info from Piano and registers them on MVault.
    """
    resp = requests.put(
        url=Config.MVAULT_API + "memberships/" + user_id + "/",
        auth=(Config.MVAULT_KEY, Config.MVAULT_SECRET),
        headers={'Content-type': 'application/json'},
        data=json.dumps(register_data)
    )
    if resp.ok:
        print('Successfully added user ' + register_data['email'] + ' to pbs passport')
        response_dict = json.loads(resp.content)
        mvault_id = response_dict["mvault_id"]
        activation_token = response_dict["token"]
        return mvault_id, activation_token
    else:
        print('Could not add user ' + register_data['email'] + ' to pbs passport')
        print(resp.content, file=sys.stderr)
    return None, None


def add_to_pbs(user): #ignoring
    """
    Finds the user via the uid on Piano, registers them on Mvault, and
    adds them to an email list that will send their passport token.
    """
    (mvault_id, token) = register_user_on_pbs(
        "LVN-" + user.uid,
        {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "offer": "wlvt-passport-offer",
            "start_date": datetime.now().replace(tzinfo=None, microsecond=0).isoformat() + 'Z',
            "expire_date": datetime.now().replace(year=datetime.now().year + 1, tzinfo=None,
                                                  microsecond=0).isoformat() + 'Z'
        }
    )
    if mvault_id:
        add_mvault_and_token_to_piano_user(mvault_id, token, user)


def add_to_campaign_monitor(data, user, donation_data, list_id):
    """
    Adds the user to the appropriate lists on campaign monitor
    """
    if Config.CAMPAIGN_MONITOR_API_URL and not is_subscribed_to_campaign_monitor(user.email, list_id):
        resp = requests.post(
            url=Config.CAMPAIGN_MONITOR_API_URL
                + "/subscribers/"
                + list_id
                + ".json",
            headers={'Content-type': 'application/json'},
            auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
            data=json.dumps({
                "EmailAddress": user.email,
                "Name": user.personal_name,
                "CustomFields": [
                    {"Key": "firstname", "Value": user.first_name or ""},
                    {"Key": "lastname", "Value": user.last_name or ""},
                    # {"Key": "piano_uid", "Value": data.uid or ""},
                    {"Key": "donation_start", "Value": donation_data["donation_start"] or ""},
                    {"Key": "donation_amount", "Value": donation_data["donation_amount"] or ""},
                    {"Key": "donation_frequency", "Value": donation_data["donation_frequency"] or ""},
                    {"Key": "donation_expiration", "Value": donation_data["donation_expiration"] or ""},
                ],
                "Resubscribe": True,
                "RestartSubscriptionBasedAutoresponders": True,
                "ConsentToTrack": "Unchanged",
            })
        )
        if resp.ok:
            print('Successfully registered ' + user.email + ' to campaign monitor list ' + list_id)
        else:
            print('Registering ' + user.email + ' to campaign monitor list ' + list_id + ' failed', file=sys.stderr)
            print(resp.content, file=sys.stderr)


def is_subscribed_to_campaign_monitor(email, list_id):
    """
    Determines whether the user is subscribed to a list in campaign monitor
    """
    subscribed_resp = requests.get(
        url=Config.CAMPAIGN_MONITOR_API_URL + "/subscribers/" + list_id + ".json",
        params={'email': email},
        headers={'Content-type': 'application/json'},
        auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
    )
    if subscribed_resp.ok:
        subscribed = json.loads(subscribed_resp.content)
        return 'State' in subscribed.keys() and subscribed['State'] == 'Active'
    return False


def unsubscribe_from_campaign_monitor(email):
    """
    Unsubscribes the user to the appropriate lists on campaign monitor
    """
    if Config.CAMPAIGN_MONITOR_API_URL:
        for campaign_monitor_list in (
            Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST.split(',') +
            Config.CAMPAIGN_MONITOR_ACTIVE_DONORS_REGULAR_PROD.split(',')
        ):
            if is_subscribed_to_campaign_monitor(email, campaign_monitor_list):
                # Only unsubscribe if subscribed
                resp = requests.post(
                    url=Config.CAMPAIGN_MONITOR_API_URL
                        + "/subscribers/"
                        + campaign_monitor_list
                        + "/unsubscribe.json",
                    headers={'Content-type': 'application/json'},
                    auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
                    data=json.dumps({"EmailAddress": email})
                )
                if resp.ok:
                    print('Successfully unsubscribed ' + email + ' to campaign monitor list ' + campaign_monitor_list)
                else:
                    print('Unsubscribing ' + email + ' to campaign monitor list ' + campaign_monitor_list + ' failed', file=sys.stderr)
                    print(resp.content, file=sys.stderr)


def add_piano_esp_merge_fields(user):
    merge_fields = []
    if "first_name" in user:
        merge_fields.append({"user": user["email"], "umf": "FIRSTNAME", "value": user["first_name"]})
    if "last_name" in user:
        merge_fields.append({"user": user["email"], "umf": "LASTNAME", "value": user["last_name"]})
    # if "personal_name" in user:
    #     merge_fields.append({"user": user["email"], "umf": "PERSONALNAME", "value": user["personal_name"]})
    # if "uid" in user:
        # merge_fields.append({"user": user["email"], "umf": "USERID", "value": user["uid"]})
    if "adid" in user:
        merge_fields.append({"user": user["email"], "umf": "ADID", "value": user["adid"]})
    if "donation_status" in user:
        merge_fields.append({"user": user["email"], "umf": "DONATIONSTATUS", "value": user["donation_status"]})
    if "donation_amount" in user:
        merge_fields.append({"user": user["email"], "umf": "DONATIONAMOUNT", "value": user["donation_amount"]})

    resp = requests.post(
        url=Config.PIANO_ESP_API_URL + "/userdata/umfval/pub/" + Config.PIANO_ESP_SITE_ID + "/set",
        params={'api_key': Config.PIANO_ESP_API_KEY},
        headers={'Content-type': 'application/json'},
        data=json.dumps(merge_fields)
    )
    if resp.ok:
        print('Successfully added merge fields to ' + user["email"] + ' in piano esp')
    else:
        print('Adding merge fields to ' + user["email"] + ' in piano esp failed', file=sys.stderr)
        print(resp.content, file=sys.stderr)


def add_to_piano_esp(user, donation_data, list_id):
    """
    Adds the user to the correct list on piano ESP
    """
    updated_user = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        # "personal_name": user.personal_name,
        # "uid": user.uid,
        "adid": re.sub(
            r'[^A-Za-z0-9]+',
            '',
            base64.b32encode(bytearray(user.email, 'ascii')).decode('utf-8')
        ),
        "donation_status": donation_data["donated"],
        "donation_amount": donation_data["donation_amount"], 
    }
    if Config.PIANO_ESP_API_URL and not is_subscribed_to_piano_esp(user.email, list_id):
        resp = requests.post(
            url=Config.PIANO_ESP_API_URL + "/tracker/securesub",
            params={'api_key': Config.PIANO_ESP_API_KEY},
            headers={'Content-type': 'application/x-www-form-urlencoded'},
            data=({"email": user.email, "mlids": list_id})
        )
        if resp.ok:
            print('Successfully registered ' + user.email + ' to piano esp list ' + list_id)
            print(resp.content)
            # Add merge fields
            add_piano_esp_merge_fields(updated_user)
        else:
            print('Registering ' + user.email + ' to piano esp list ' + list_id + ' failed', file=sys.stderr)
            print(resp.content, file=sys.stderr)
    if Config.PIANO_ESP_API_URL and is_subscribed_to_piano_esp(user.email, list_id) == True:
        print('Updating existing user ' + updated_user)
        add_piano_esp_merge_fields(updated_user)


def get_subscribed_lists_piano_esp(email):
    if Config.PIANO_ESP_API_URL:
        # Check if subscribed
        all_mlids = (Config.PIANO_ESP_REGISTERED_USERS_LIST + ',' + Config.PIANO_ESP_PLUS_USERS_LIST).split(',')
        subscribed_mlids = []
        for mlid in all_mlids:
            subscribed_resp = requests.get(
                url=Config.PIANO_ESP_API_URL + "/tracker/securesub/email/" + email + "/ml/" + mlid,
                params={'api_key': Config.PIANO_ESP_API_KEY},
            )
            if subscribed_resp.ok:
                subscribed_mlids.append(mlid)
        print(subscribed_mlids)
        return subscribed_mlids
    return []


def is_subscribed_to_piano_esp(email, list_id):
    """
    Determines whether the user is subscribed to a list in piano esp
    """
    return list_id in get_subscribed_lists_piano_esp(email)


def unsubscribe_from_piano_esp(email):
    """
    Removes the user from all lists on piano ESP
    """
    if Config.PIANO_ESP_API_URL:
        subscribed_mlids = get_subscribed_lists_piano_esp(email)

        if len(subscribed_mlids) > 0:
            resp = requests.delete(
                url=Config.PIANO_ESP_API_URL + "/tracker/securesub",
                params={'api_key': Config.PIANO_ESP_API_KEY},
                headers={'Content-type': 'application/x-www-form-urlencoded'},
                data=({
                    "email": email,
                    "mlids": ','.join(subscribed_mlids)
                })
            )
            if resp.ok:
                print('Successfully unsubscribed ' + email + ' from piano esp')
            else:
                print('Unsubscribing ' + email + ' from piano esp failed', file=sys.stderr)
                print(resp.content, file=sys.stderr)


def register_campaign_monitor_webhook(cm_list):
    """
    Registers the webhook on Campaign Monitor
    https://www.campaignmonitor.com/api/v3-3/lists/#creating-a-webhook
    """
    if Config.APP_WEBHOOKS_URL:
        # Get and clear all existing webhooks
        resp = requests.get(
            url=Config.CAMPAIGN_MONITOR_API_URL + "/lists/" + cm_list + "/webhooks.json",
            headers={'Content-type': 'application/json'},
            auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x')
        )
        if resp.ok:
            webhooks = json.loads(resp.content)
            for webhook in webhooks:
                resp2 = requests.delete(
                    url=Config.CAMPAIGN_MONITOR_API_URL + "/lists/" + cm_list + "/webhooks/" + webhook['WebhookID'] + ".json",
                    headers={'Content-type': 'application/json'},
                    auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x')
                )
                if resp2.ok:
                    print('Successfully deleted unsubscribe webhook ' + webhook['WebhookID']
                          + ' on Campaign Monitor on list ' + cm_list)
                # else if an error, but not the error that it doesn't exist (code 699)
                elif json.loads(resp2.content)['Code'] != 699:
                    print('Deleting unsubscribe webhook ' + webhook['WebhookID']
                          + ' on Campaign Monitor on list ' + cm_list + ' failed')
                    print(resp2.content, file=sys.stderr)

        else:
            print('Getting webhooks on Campaign Monitor on list ' + cm_list + ' failed', file=sys.stderr)
            print(resp.content, file=sys.stderr)

        # Sleep for 10 second to allow other workers to boot
        time.sleep(10)

        # Create webhook
        resp = requests.post(
            url=Config.CAMPAIGN_MONITOR_API_URL + "/lists/" + cm_list + "/webhooks.json",
            headers={'Content-type': 'application/json'},
            auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
            data=json.dumps({
                "Events": ["Deactivate"],
                "Url": Config.APP_WEBHOOKS_URL,
                "PayloadFormat": "json"
            })
        )
        if resp.ok:
            print('Successfully registered unsubscribe webhook with Campaign Monitor on list ' + cm_list)
        else:
            print('Registering unsubscribe webhook with Campaign Monitor failed on list ' + cm_list, file=sys.stderr)
            print(resp.content, file=sys.stderr)
    else:
        print('APP_WEBHOOKS_URL env variable not set', file=sys.stderr)


def process_piano_webhook(request):
    # Piano Webhook
    if request.method == 'GET':
        try:
            webhook_data = PIANO_CLIENT.parse_webhook_data(request.args["data"])
            # Get the user data from the piano api
            user = PIANO_CLIENT.publisher_user_api.get(aid=webhook_data.aid, uid=webhook_data.uid).data
            donation_data = {
                "donated": False,
                "donation_start": "",
                "donation_amount": 0, 
                "donation_frequency": "N/A",
                "donation_expiration": "N/A"
            }

            print('Received piano webhook for ' + webhook_data.event)
            # See if the event is a new registration
            if webhook_data.event in ['new_purchase', 'free_access_granted', 'user_created']:
                if hasattr(webhook_data, 'rid') and \
                        (webhook_data.rid != Config.LV_FREE_RESOURCE_ID #keep this line
                         and 
                         webhook_data.rid != Config.LV_PLUS_RESOURCE_ID): #remove this line
                    # user_created event doesn't have an RID!
                    # if webhook_data.event == 'new_purchase':
                    term = PIANO_CLIENT.publisher_term_api.get(term_id=webhook_data.term_id).data
                    donation_data["donated"] = True
                    donation_data["donation_start"] = datetime.today().isoformat()
                    donation_data["donation_amount"] = term.payment_billing_plan_table[0]["priceAndTax"]
                    donation_data["donation_frequency"] = term.payment_billing_plan_table[0]["period"]
                    if term.payment_billing_plan_table[0]["period"] == "year":
                        donation_data["donation_expiration"] = (datetime.today() + relativedelta(years=1)).isoformat()
                    else: 
                        donation_data["donation_expiration"] = (datetime.today() + relativedelta(months=1)).isoformat()
                    
                    if Config.PIANO_ESP_REGISTERED_USERS_LIST:
                        add_to_piano_esp(user, donation_data, Config.PIANO_ESP_REGISTERED_USERS_LIST)
                    if Config.CAMPAIGN_MONITOR_ACTIVE_DONORS_REGULAR_PROD:
                        for list_id in Config.CAMPAIGN_MONITOR_ACTIVE_DONORS_REGULAR_PROD.split(','):
                            add_to_campaign_monitor(webhook_data, user, donation_data, list_id)

                elif hasattr(webhook_data, 'rid') and (webhook_data.rid == Config.LV_PLUS_RESOURCE_ID): #remove this chunk
                    if Config.PIANO_ESP_PLUS_USERS_LIST:
                        add_to_piano_esp(user, donation_data, Config.PIANO_ESP_PLUS_USERS_LIST)
                    if Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST:
                        for list_id in Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST.split(','):
                            add_to_campaign_monitor(webhook_data, user, donation_data, list_id)
                else:
                # Adds this user to the registered users list
                    if Config.PIANO_ESP_REGISTERED_USERS_LIST:
                        add_to_piano_esp(user, donation_data, Config.PIANO_ESP_REGISTERED_USERS_LIST)
                    if Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST:
                        for list_id in Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST.split(','):
                            add_to_campaign_monitor(webhook_data, user, donation_data, list_id)
                return "User Registered Successfully"

            # TODO if user changed email / name / other details
        except ValueError as e:
            print(e, file=sys.stderr)

    # Piano ESP Webhook
    #
    # Note: The only way to set up a piano esp webhook url is to email them. Currently,
    # they are set to:
    # production: https://lvn-ux-server.herokuapp.com/webhooks
    # sandbox: https://lvn-sandbox-ux-server.herokuapp.com/webhooks
    elif request.method == 'POST':
        request_data = request.get_json()

        if 'action' in request_data.keys() and request_data['action'] == 'user_removed':
            unsubscribe_from_campaign_monitor(request_data['email'])
        # New email subscription to newsletter
        if 'action' in request_data.keys() and request_data['action'] == 'user_added':
            add_piano_esp_merge_fields({
                'email': request_data['email'],
                'adid': base64.b32encode(bytearray(request_data['email'], 'ascii')).decode('utf-8')
            })
            print('Added mergefields to new email subscriber ' + request_data['email'])

    return "Webhook failed"


def process_campaign_monitor_webhook(request):
    # Campaign monitor sends a list of events that we loop through and handle
    # Note: currently disabled because we do not want unsubscribes in campaign monitor (the marketing emails)
    #       to also unsubscribe users from piano esp (the editorial emails)
    # request_data = request.get_json()
    # for event in request_data['Events']:
    #    if event['Type'] == 'Deactivate':
    #        unsubscribe_from_piano_esp(event['EmailAddress'])

    return "Success"
