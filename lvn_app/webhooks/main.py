from lvn_app.config import Config
from pianosdk import Client
from datetime import datetime
import requests
import json
import sys

PIANO_CLIENT = Client(api_host=Config.PIANO_HOST, api_token=Config.PIANO_API_TOKEN,
                      private_key=Config.PIANO_PRIVATE_KEY)


def add_mvault_and_token_to_piano_user(mvault_id: str, token: str, user_id: str):
    """
    Takes the Mvault ID and Token String returned from the Mvault API and
    saves them on the User record in Piano.
    Note: The feature to update custom fields from the Piano python SDK wasn't working,
    so we're contacting the API directly here.
    """
    requests.post(
        url=Config.PIANO_API_URL
            + "/publisher/user/update?aid="
            + Config.PIANO_APP_ID
            + "&api_token=" + Config.PIANO_API_TOKEN + "&uid=" + user_id,
        headers={'Content-type': 'application/json'},
        auth=(Config.MVAULT_KEY, Config.MVAULT_SECRET),
        data=json.dumps({
            "passport-auth": token,  # TODO: Ask Kit if we can change passport-auth to passport_auth
            "mvault_id": mvault_id
        })
    )


def register_user_on_pbs(user_id: str, register_data):
    """
    Takes the user info from Piano and registers them on MVault.
    """
    response = requests.put(
        url=Config.MVAULT_API + "memberships/" + user_id + "/",
        auth=(Config.MVAULT_KEY, Config.MVAULT_SECRET),
        headers={'Content-type': 'application/json'},
        data=json.dumps(register_data)
    )
    response_dict = json.loads(response.content)
    mvault_id = response_dict["mvault_id"]
    activation_token = response_dict["token"]
    return (mvault_id, activation_token)


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
    add_mvault_and_token_to_piano_user(mvault_id, token, user.uid)


def add_to_campaign_monitor(data, user):
    """
    Adds the user to the appropriate lists on campaign monitor
    """
    # TODO determine which list we are adding to
    requests.post(
        url=Config.CAMPAIGN_MONITOR_API_URL
            + "/subscribers/"
            + Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST
            + ".json",
        headers={'Content-type': 'application/json'},
        auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
        data=json.dumps({
            "EmailAddress": user.email,
            "Name": user.personal_name,
            "CustomFields": [
                {
                    "Key": "firstname",
                    "Value": user.first_name
                },
                {
                    "Key": "lastname",
                    "Value": user.last_name
                },
                {
                    "Key": "piano_uid",
                    "Value": data.uid
                },
            ],
            "Resubscribe": True,
            "RestartSubscriptionBasedAutoresponders": True,
            "ConsentToTrack": "Unchanged",
        })
    )


def add_to_piano_esp(user, list_id):
    """
    Adds the user to the correct list on piano ESP
    """
    if Config.PIANO_ESP_API_URL:
        resp = requests.post(
            url=Config.PIANO_ESP_API_URL + "/tracker/securesub?api_key=" + Config.PIANO_API_TOKEN,
            headers={'Content-type': 'application/x-www-form-urlencoded'},
            data=({"email": user.email, "mlids": [list_id]})
        )
        if resp.ok:
            print('Successfully registered ' + user.email + ' to piano esp list ' + list_id)
        else:
            print('Registering ' + user.email + ' to piano esp list ' + list_id + ' failed.', file=sys.stderr)
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
            print('Registering unsubscribe webhook with Campaign Monitor failed.', file=sys.stderr)
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
            add_to_campaign_monitor(webhook_data, user)

            # If this user is newly registered to lv+, we also add to pbs passport
            if webhook_data.rid == Config.LV_PLUS_RESOURCE_ID:
                add_to_pbs(user)
                if Config.PIANO_ESP_PLUS_USERS_LIST:
                    add_to_piano_esp(user, Config.PIANO_ESP_PLUS_USERS_LIST)

            # Adds this user to the registered users list
            if Config.PIANO_ESP_REGISTERED_USERS_LIST:
                add_to_piano_esp(user, Config.PIANO_ESP_REGISTERED_USERS_LIST)
            return "User Registered Successfully"

        # TODO if this is an unsubscribe
        # TODO if user changed email / name / other details
    except ValueError as e:
        print(e, file=sys.stderr)

    return "Webhook failed"


def process_campaign_monitor_webhook(request):
    pass
