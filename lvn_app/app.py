from flask import Flask, request
from lvn_app.webhooks.main import process_data
from lvn_app.config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/webhooks')
def webhooks():
    response = process_data(request.args["data"])
    print(f'Webhook event: [{type(response)}] {response}')
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)