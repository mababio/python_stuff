# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
import os
import boto3
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from config import config

key_id= config.aws_access_key_id
key= config.aws_secret_access_key
phone_num = config.phone_to

def create_client():
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        region_name="us-east-1"
    )
    return client

def sms(message):
    client = create_client()
    # Send your sms message.
    client.publish(
        PhoneNumber=config.phone_to,
        Message=message
    )


def email():
    pass
