
"""
Author: Michael Ababio
Date: 02-06-2017
Purpose: centralize point for define app config values
"""

import configparser
import os


CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH + '/config.ini')


PHONE_NUM_TO = CONFIG['TWILIO']['phone_num_to'].strip("''")
PHONE_NUM_FROM = CONFIG['TWILIO']['phone_num_from'].strip("'")
ACCOUNT_SID = CONFIG['TWILIO']['account_sid'].strip("'")
AUTH_TOKEN = CONFIG['TWILIO']['auth_token'].strip("'")
