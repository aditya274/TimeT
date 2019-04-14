from twilio.rest import Client
import datetime
import time
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def timet():
	count = 0
	while(True):
		days = ["monday.txt", "tuesday.txt", "wednesday.txt", "thursday.txt", "friday.txt", "saturday.txt", "sunday.txt"]
		d = datetime.datetime.today().weekday()

		account_sid = "ACb8d91a3df5c33396b226bb1cee1b85b5"
		auth_token = "93456d7a03cbd46568978f47aed90011"

		mobile_number = ["+919936284777",]
		for i in mobile_number:
			f = open('days/'+days[d], 'r')
			client = Client(account_sid, auth_token)
			message = client.messages.create(from_='whatsapp:+14155238886', body= f.read(), to='whatsapp:'+ i)
			f.close()
		f.close()
		count += 1
		if count == 5:
			break
		time.sleep(5)

	reply = ""
	days = ["monday.txt", "tuesday.txt", "wednesday.txt", "thursday.txt", "friday.txt", "saturday.txt", "sunday.txt"]
	d = datetime.datetime.today().weekday()
	f = open('days/'+days[d], 'r')
	body = request.values.get('Body', None)
	if 'update' in body.lower():
		reply = f.read()
		f.close()
	
	elif 'broadcast' in body.lower():
		msg = "Broadcast from " + str(request.values.get('From', None))[-13:] + ":\n" + body[10:]
		account_sid = "ACb8d91a3df5c33396b226bb1cee1b85b5"
		auth_token = "93456d7a03cbd46568978f47aed90011"

		mobile_number = ["+919936284777", "+919260972911", "+919755761191", "+917448009954", "+917004727387"]
		for i in mobile_number:
			f = open('days/'+days[d], 'r')
			client = Client(account_sid, auth_token)
			message = client.messages.create(from_='whatsapp:+14155238886', body= msg, to='whatsapp:'+ i)
		f.close()
		reply = "Message broadcasted."

	else: reply = "Have a good day!"

	resp = MessagingResponse()
	resp.message(reply) 
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)