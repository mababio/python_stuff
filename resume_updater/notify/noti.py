# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
import os
import boto3
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from config import config

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key,
    region_name="us-east-1"
)

def sms(message):
    # Send your sms message.
    client.publish(
        PhoneNumber=config.phone_to,
        Message=message
    )


def email():
    pass
