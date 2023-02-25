from lvn_app.config import Config
from pianosdk import Client
from datetime import datetime
import requests
import json
import sys

PIANO_CLIENT = Client(api_host=Config.PIANO_HOST, api_token=Config.PIANO_API_TOKEN, private_key=Config.PIANO_PRIVATE_KEY)

"""
Takes the Mvault ID and Token String returned from the Mvault API and
saves them on the User record in Piano.
Note: The feature to update custom fields from the Piano python SDK wasn't working,
so we're contacting the API directly here.
"""
def add_mvault_and_token_to_piano_user(mvault_id: str, token: str, user_id: str):
    requests.post(
        url=Config.PIANO_API_URL
            +"/publisher/user/update?aid="
            +Config.PIANO_APP_ID
            +"&api_token="+Config.PIANO_API_TOKEN+"&uid="+user_id,
        headers={'Content-type': 'application/json'},
        auth=(Config.MVAULT_KEY, Config.MVAULT_SECRET),
        data=json.dumps({
            "passport-auth": token, # TODO: Ask Kit if we can change passport-auth to passport_auth
            "mvault_id": mvault_id  
        })
    )

"""
Takes the user info from Piano and registers them on MVault.
"""
def register_user_on_pbs(user_id: str, register_data):
    response = requests.put(
        url=Config.MVAULT_API + "memberships/" +  user_id + "/",
        auth=(Config.MVAULT_KEY, Config.MVAULT_SECRET),
        headers={'Content-type': 'application/json'},
        data=json.dumps(register_data)
    )
    response_dict = json.loads(response.content)
    mvault_id = response_dict["mvault_id"]
    activation_token = response_dict["token"]
    return (mvault_id, activation_token)

"""
Finds the user via the uid on Piano, registers them on Mvault, and
adds them to an email list that will send their passport token.
"""
def add_to_pbs(data):
    user = PIANO_CLIENT.publisher_user_api.get(
        aid=data.aid,
        uid=data.uid,
    ).data
    (mvault_id, token) = register_user_on_pbs(
        "LVN-" + user.uid,
        {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "offer": "wlvt-passport-offer",
            "start_date": datetime.now().replace(tzinfo=None, microsecond=0).isoformat() + 'Z',
            "expire_date": datetime.now().replace(year=datetime.now().year + 1, tzinfo=None, microsecond=0).isoformat() + 'Z'
        }
    )
    add_mvault_and_token_to_piano_user(mvault_id, token, user.uid)

"""
Adds the user to the appropriate lists on campaign monitor
"""
def add_to_campaign_monitor(data):
    user = PIANO_CLIENT.publisher_user_api.get(
        aid=data.aid,
        uid=data.uid,
    ).data

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

"""
Adds the user to the correct list on piano ESP
"""
def add_to_piano_esp(data):
    # TODO add this user to the lists on piano esp
    pass

"""
Registers the webhook on Campaign Monitor
https://www.campaignmonitor.com/api/v3-3/lists/#creating-a-webhook
"""
def register_campaign_monitor_webhook():
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
        if not resp.ok:
            print('Registering unsubscribe webhook with Campaign Monitor failed.', file=sys.stderr)
            print(resp.content, file=sys.stderr)
    pass

def process_data(data):
    # TODO Determine where this webhook is coming from: Piano? Piano ESP? Campaign Monitor?
    # TODO add some validation to prevent webhooks from being spoofed
    webhook_data = PIANO_CLIENT.parse_webhook_data(data)
    # if webhook_data.event in webhook_events and webhook_data.rid == Config.LV_PLUS_RESOURCE_ID:
    if (webhook_data.event == 'new_purchase' or webhook_data.event == 'free_access_granted') and webhook_data.rid == Config.LV_PLUS_RESOURCE_ID:
        add_to_pbs(webhook_data)
        add_to_campaign_monitor(webhook_data)
    return "User Registered to Mvault Successfully"
