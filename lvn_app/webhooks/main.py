from lvn_app.config import Config
from pianosdk import Client
from datetime import datetime
import requests
import json
import sys

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
        print('Successfully added user ' + register_data.email + ' to pbs passport')
        response_dict = json.loads(resp.content)
        mvault_id = response_dict["mvault_id"]
        activation_token = response_dict["token"]
        return (mvault_id, activation_token)
    else:
        print('Could not add user ' + register_data.email + ' to pbs passport')
        print(resp.content, file=sys.stderr)
    return (None, None)


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
            data=({"email": user.email, "mlids": [list_id.split(',')]})
        )
        if resp.ok:
            print('Successfully registered ' + user.email + ' to piano esp list ' + list_id)
            # Add merge fields
            resp2 = requests.post(
                url=Config.PIANO_ESP_API_URL + "/userdata/umfval/pub/" + Config.PIANO_ESP_SITE_ID + "/set",
                params={'api_key': Config.PIANO_ESP_API_KEY},
                headers={'Content-type': 'application/x-www-form-urlencoded'},
                data=([
                    {"user": user.uid, "umf": "FIRSTNAME", "value": user.first_name},
                    {"user": user.uid, "umf": "LASTNAME", "value": user.last_name},
                    {"user": user.uid, "umf": "PERSONALNAME", "value": user.personal_name}
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


def register_campaign_monitor_webhook():
    """
    Registers the webhook on Campaign Monitor
    https://www.campaignmonitor.com/api/v3-3/lists/#creating-a-webhook
    """
    if Config.APP_WEBHOOKS_URL:
        resp = requests.post(
            url=Config.CAMPAIGN_MONITOR_API_URL
                + "/lists/"
                + Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST
                + "/webhooks.json",
            headers={'Content-type': 'application/json'},
            auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
            data=json.dumps({
                "Events": ["Deactivate"],
                "Url": Config.APP_WEBHOOKS_URL,
                "PayloadFormat": "json"
            })
        )
        if resp.ok:
            print('Successfully registered unsubscribe webhook with Campaign Monitor.')
        else:
            print('Registering unsubscribe webhook with Campaign Monitor failed', file=sys.stderr)
            print(resp.content, file=sys.stderr)
    else:
        print('APP_WEBHOOKS_URL env variable not set.', file=sys.stderr)


def process_piano_webhook(request):
    try:
        webhook_data = PIANO_CLIENT.parse_webhook_data(request.args["data"])

        # Get the user data from the piano api
        user = PIANO_CLIENT.publisher_user_api.get(aid=webhook_data.aid, uid=webhook_data.uid).data

        # See if the event is a new registration
        if webhook_data.event in ['new_purchase', 'free_access_granted']:
            if webhook_data.rid == Config.LV_PLUS_RESOURCE_ID:
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
        # TODO if user changed email / name / other details
    except ValueError as e:
        print(e, file=sys.stderr)

    return "Webhook failed"


def process_campaign_monitor_webhook(request):
    pass
