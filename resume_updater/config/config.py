import configparser
import os
import json

config_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(config_path + '/config.ini')


phone_num_to = config['TWILIO']['phone_num_to'].strip("''")
phone_num_from = config['TWILIO']['phone_num_from'].strip("'")
account_sid = config['TWILIO']['account_sid'].strip("'")
auth_token = config['TWILIO']['auth_token'].strip("'")
