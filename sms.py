from twilio .rest import TwilioRestClient
from flask import Flask, request
from twilio import twiml

client = TwilioRestClient()

client.messages.create(from_="",to="",body="")



app = Flask(__name__)

@app.route('/msg',methods=['POST'])
def msg():
	number = request.form['no']
	msgb = request.form['msg']

	resp = twilio.Response()
	resp.message('hello {}, you sii {}'.format(number,msgb))
	return str(resp)

if __name__ == '__main__':
	app.run()
