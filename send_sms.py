#twilio integration file

# Download the twilio-python library from http://twilio.com/docs/libraries
# pip install twilio should work, otherwise use easy_install twilio
import sys
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
# Hidden for Privacy
account_sid = ""
auth_token = ""

account_sid = "AC93bc79a222d23f5e7e09308591e8bec2"
auth_token = "ceef4b2d00ddca1ddc4b73ede5bc4539"

client = TwilioRestClient(account_sid, auth_token)

# Call at the beginning of the day to remind them what medications they have today so they can prepare accordingly
def dailyMedicationReminder():
	msg = "Reminder to take your medication today!"
	print msg
	
# Call when you need to remind them to take their medication (e.g. 5 minutes before prescription's detail)
def medicationReminder():
	msg = "Remember to take your medication in a few minutes!"
	print msg

if (int(sys.argv[1]) != 1):
	dailyMedicationReminder()
# 	print msg
else:
	medicationReminder()
# 	print msg
	
# message = client.messages.create(to="+14088934962", from_="+14083421269",
#                                      body=msg)