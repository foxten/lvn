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

    # Campaign monitor uses a POST webhook
    # https://www.campaignmonitor.com/api/v3-3/webhooks/
    elif request.method == 'POST':
        return process_campaign_monitor_webhook(request)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# Register the webhooks we need
register_campaign_monitor_webhook()
