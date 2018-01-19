# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from config import config


def sms(message):
    client = Client(config.account_sid, config.auth_token)
    client.api.account.messages.create(
        to= config.phone_num_to,
        from_=config.phone_num_from,
        body=message)



sms("hello, mike!")
