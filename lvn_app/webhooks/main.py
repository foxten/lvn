from lvn_app.config import Config
from pianosdk import Client
from datetime import datetime
import requests
import json

PIANO_CLIENT = Client(api_host=Config.PIANO_HOST, api_token=Config.PIANO_API_TOKEN, private_key=Config.PIANO_PRIVATE_KEY)

"""
Takes the Mvault ID and Token String returned from the Mvault API and
saves them on the User record in Piano.
Note: The feature to update custom fields from the Piano python SDK wasn't working,
so we're contacting the API directly here.
"""
def add_mvault_and_token_to_piano_user(mvault_id: str, token: str, user_id: str):
    requests.post(
        url="https://sandbox.piano.io/api/v3/publisher/user/update?aid="
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

def process_data(data):
    webhook_data = PIANO_CLIENT.parse_webhook_data(data)
    if webhook_data.event == 'new_purchase' and webhook_data.rid == Config.LV_PLUS_RESOURCE_ID:
        add_to_pbs(webhook_data)
    return "User Registered to Mvault Successfully"