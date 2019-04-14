from twilio.rest import Client
import datetime
days = ["monday.txt", "tuesday.txt", "wednesday.txt", "thursday.txt", "friday.txt", "saturday.txt", "sunday.txt"]

d = datetime.datetime.today().weekday()
print "Today is: " +days[d][0].upper() + days[d][1:-4]

account_sid = "ACb8d91a3df5c33396b226bb1cee1b85b5"
auth_token = "93456d7a03cbd46568978f47aed90011"

#f = open(days/days[d], 'r')
mobile_number = ["+919936284777",]
for i in mobile_number:
	f = open('days/'+days[d], 'r')
	client = Client(account_sid, auth_token)
	message = client.messages.create(from_='whatsapp:+14155238886', body= f.read(), to='whatsapp:'+ i)
	f.close()
	print message.sid 

f.close()

