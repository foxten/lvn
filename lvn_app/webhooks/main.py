from lvn_app.config import Config
from pianosdk import Client
from datetime import datetime
import requests
import json
import sys
import time

PIANO_CLIENT = Client(api_host=Config.PIANO_HOST, api_token=Config.PIANO_API_TOKEN,
                      private_key=Config.PIANO_PRIVATE_KEY)


def add_mvault_and_token_to_piano_user(mvault_id: str, token: str, user):
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
        resp = requests.put(
            url=Config.CAMPAIGN_MONITOR_API_URL
                + "/subscribers/"
                + Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST
                + ".json",
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


def register_user_on_pbs(user_id: str, register_data):
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


def add_to_pbs(user):
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


def add_to_campaign_monitor(data, user, list_id):
    """
    Adds the user to the appropriate lists on campaign monitor
    """
    if Config.CAMPAIGN_MONITOR_API_URL:
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
                    {"Key": "firstname", "Value": user.first_name},
                    {"Key": "lastname", "Value": user.last_name},
                    {"Key": "piano_uid", "Value": data.uid},
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


def add_to_piano_esp(user, list_id):
    """
    Adds the user to the correct list on piano ESP
    """
    if Config.PIANO_ESP_API_URL:
        resp = requests.post(
            url=Config.PIANO_ESP_API_URL + "/tracker/securesub",
            params={'api_key': Config.PIANO_ESP_API_KEY},
            headers={'Content-type': 'application/x-www-form-urlencoded'},
            data=({"email": user.email, "mlids": list_id})
        )
        if resp.ok:
            print('Successfully registered ' + user.email + ' to piano esp list ' + list_id)
            # Add merge fields
            resp2 = requests.post(
                url=Config.PIANO_ESP_API_URL + "/userdata/umfval/pub/" + Config.PIANO_ESP_SITE_ID + "/set",
                params={'api_key': Config.PIANO_ESP_API_KEY},
                headers={'Content-type': 'application/json'},
                data=json.dumps([
                    {"user": user.email, "umf": "FIRSTNAME", "value": user.first_name},
                    {"user": user.email, "umf": "LASTNAME", "value": user.last_name},
                    {"user": user.email, "umf": "PERSONALNAME", "value": user.personal_name}
                ])
            )
            if resp2.ok:
                print('Successfully added merge fields to ' + user.email + ' in piano esp')
            else:
                print('Adding merge fields to ' + user.email + ' in piano esp failed', file=sys.stderr)
                print(resp2.content, file=sys.stderr)
        else:
            print('Registering ' + user.email + ' to piano esp list ' + list_id + ' failed', file=sys.stderr)
            print(resp.content, file=sys.stderr)


def remove_from_piano_esp(email):
    """
    Removes the user from all lists on piano ESP
    """
    if Config.PIANO_ESP_API_URL:
        resp = requests.delete(
            url=Config.PIANO_ESP_API_URL + "/tracker/securesub",
            params={'api_key': Config.PIANO_ESP_API_KEY},
            headers={'Content-type': 'application/x-www-form-urlencoded'},
            data=({
                "email": email,
                "mlids": Config.PIANO_ESP_REGISTERED_USERS_LIST + ',' + Config.PIANO_ESP_PLUS_USERS_LIST
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
    try:
        webhook_data = PIANO_CLIENT.parse_webhook_data(request.args["data"])

        # Get the user data from the piano api
        user = PIANO_CLIENT.publisher_user_api.get(aid=webhook_data.aid, uid=webhook_data.uid).data

        print('Received piano webhook for ' + webhook_data.event)
        # See if the event is a new registration
        if webhook_data.event in ['new_purchase', 'free_access_granted', 'user_created']:
            if hasattr(webhook_data, 'rid') and webhook_data.rid == Config.LV_PLUS_RESOURCE_ID:
                if Config.PIANO_ESP_PLUS_USERS_LIST:
                    add_to_piano_esp(user, Config.PIANO_ESP_PLUS_USERS_LIST)
                if Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST:
                    add_to_campaign_monitor(webhook_data, user, Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST)
                # If this user is newly registered to lv+, we also add to pbs passport
                add_to_pbs(user)

            # Adds this user to the registered users list
            if Config.PIANO_ESP_REGISTERED_USERS_LIST:
                add_to_piano_esp(user, Config.PIANO_ESP_REGISTERED_USERS_LIST)
            if Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST:
                add_to_campaign_monitor(webhook_data, user, Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST)
            return "User Registered Successfully"

        # TODO if this is an unsubscribe
        # Note: The only way to set up a piano esp webhook url is to email them. Currently,
        # they are set to:
        # production: https://lvn-ux-server.herokuapp.com/webhooks
        # sandbox: https://lvn-sandbox-ux-server.herokuapp.com/webhooks

        # TODO if user changed email / name / other details
        # TODO registered user upgrade
    except ValueError as e:
        print(e, file=sys.stderr)

    return "Webhook failed"


def process_campaign_monitor_webhook(request):
    # Campaign monitor sends a list of events that we loop through and handle
    request_data = request.get_json()
    for event in request_data['Events']:
        if event['Type'] == 'Deactivate':
            remove_from_piano_esp(event['EmailAddress'])

    return "Success"
