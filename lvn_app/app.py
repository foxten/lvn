from flask import Flask, request
from lvn_app.webhooks.main import process_data, register_campaign_monitor_webhook
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi the LVN server is running"
    
@app.route('/webhooks')
def webhooks():
    print(request.headers)
    response = process_data(request.args["data"])
    print(f'Webhook event: {response}')
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    register_campaign_monitor_webhook()
