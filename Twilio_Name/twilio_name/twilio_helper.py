# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import argparse
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from config import config

client = Client(config.account_sid, config.auth_token)

def get_name(phone_num):
        try:
            client_obj =  client.lookups.phone_numbers("+1"+ phone_num).fetch(type="caller-name", )
        except TwilioException as e:
                        print('fun' + e)

        return client_obj.caller_name['caller_name']


def main():
        parser =  argparse.ArgumentParser()
        parser.add_argument("num", help=" 7 digit phone number", type=int)
        args = parser.parse_args()

        val  =get_name(str(args.num))
        print(val)

if __name__ =="__main__":
        main()
