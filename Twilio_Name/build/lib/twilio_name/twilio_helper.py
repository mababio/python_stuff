# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import argparse


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)







def get_name(phone_num): 
	client_obj =  client.lookups.phone_numbers("+1"+ phone_num).fetch(type="caller-name", )
	return client_obj.caller_name['caller_name']



def main():

	parser =  argparse.ArgumentParser()
	parser.add_argument("num", help=" 7 digit phone number", type=int)
	args = parser.parse_args()
	val  = get_name(str(args.num))	
	print(val)

if __name__ =="__main__":
	#print('hello working')
	main()
