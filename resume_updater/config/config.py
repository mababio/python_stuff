import configparser
import os
import json

config_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(config_path + '/config.ini')


aws_access_key_id = str(config['TWILIO']['aws_access_key_id'].strip("\""))
aws_secret_access_key = str(config['TWILIO']['aws_secret_access_key'].strip("\""))
phone_to = str(config['TWILIO']['phone_to'].strip("\""))
