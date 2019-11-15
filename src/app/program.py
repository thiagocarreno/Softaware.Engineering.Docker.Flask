# import flask dependencies 
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request objects
    req = request.get_json()

    # fetch action from json
    if req is not None:
        action = req.get('queryResult').get('action')

    # return fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    res = jsonify(results())
    return make_response(res)

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
