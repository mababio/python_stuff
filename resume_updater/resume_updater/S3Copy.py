import boto3
import argparse
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from notify import noti
from config import config

def upload_to_s3(file):
    s3 = boto3.resource('s3')
    obj = s3.Object('mababio', 'resume.pdf')
#    try:
    obj.put(Body=open(file, 'rb'), ContentType='application/pdf', ACL='public-read')
    noti.sms("Resume was Updated.\n" +"url")
    # except StandardError:
    #     print("Unable to upload file")

def main():
        parser =  argparse.ArgumentParser()
        parser.add_argument("file", help="file path", type=str)
        args = parser.parse_args()
        upload_to_s3(str(args.file))

if __name__ =="__main__":
    main()
        
