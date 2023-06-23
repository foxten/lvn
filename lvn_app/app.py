from flask import Flask, request
from lvn_app.webhooks.main import *
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return "Hi the LVN server is running"


@app.route('/webhooks', methods=['GET', 'POST'])
def webhooks():
    # Piano puts webhooks data as a query parameter in a GET request
    # https://docs.piano.io/webhooks/
    if request.method == 'GET':
        return process_piano_webhook(request)

    elif request.method == 'POST':
        request_data = request.get_json()
        # Campaign monitor uses a POST webhook and has an "Events" key
        # https://www.campaignmonitor.com/api/v3-3/webhooks/
        if 'Events' in request_data.keys():
            return process_campaign_monitor_webhook(request)
        else:
            # Piano ESP also uses a POST request
            return process_piano_webhook(request)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# Register the webhooks we need
for campaign_monitor_list in [
    Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST,
    Config.CAMPAIGN_MONITOR_PLUS_USERS_LIST
]:
    register_campaign_monitor_webhook(campaign_monitor_list)

# Get all users in piano esp and attempt to add USERID
if Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST and Config.CAMPAIGN_MONITOR_API_URL and Config.PIANO_ESP_API_URL:
    for list_id in Config.CAMPAIGN_MONITOR_REGISTERED_USERS_LIST.split(','):
        page = 1
        numPages = 1
        while page <= numPages:
            resp = requests.get(
                url=Config.CAMPAIGN_MONITOR_API_URL
                    + "/lists/"
                    + list_id
                    + "/active.json",
                headers={'Content-type': 'application/json'},
                auth=(Config.CAMPAIGN_MONITOR_API_KEY, 'x'),
                params={'page': page},
            )
            if resp.ok:
                results = json.loads(resp.content)
                numPages = results["NumberOfPages"]
                page = page + 1
                userids = [{
                    "email": e['EmailAddress'],
                    "userid": next((f['Value'] for f in e['CustomFields'] if f['Key'] == "[piano_uid]"), "")
                } for e in results['Results']]
                for user in userids:
                    resp2 = requests.post(
                        url=Config.PIANO_ESP_API_URL + "/userdata/umfval/pub/" + Config.PIANO_ESP_SITE_ID + "/set",
                        params={'api_key': Config.PIANO_ESP_API_KEY},
                        headers={'Content-type': 'application/json'},
                        data=json.dumps([
                            {"user": user["email"], "umf": "USERID", "value": user["userid"] or ""},
                        ])
                    )
                    if resp2.ok:
                        print('Successfully updated USERID merge field for ' + user["email"] + ' in piano esp')
                    else:
                        print('Updating USERID merge field for ' + user["email"] + ' in piano esp failed', file=sys.stderr)
                        print(resp2.content, file=sys.stderr)
            else:
                print(resp.content, file=sys.stderr)