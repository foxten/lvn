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
    Config.CAMPAIGN_MONITOR_ACTIVE_DONORS_REGULAR_PROD
]:
    register_campaign_monitor_webhook(campaign_monitor_list)

