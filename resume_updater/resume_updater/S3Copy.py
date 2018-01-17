import boto3
import argparse


def upload_to_s3(file):
    s3 = boto3.resource('s3')
    obj = s3.Object('mababio', 'resume.pdf')
    obj.put(Body=open(file, 'rb'), ContentType='application/pdf', ACL='public-read')
    #'/Users/mababio/Desktop/resume/resume_v6.pdf'
def main():
        parser =  argparse.ArgumentParser()
        parser.add_argument("file", help="file path", type=str)
        args = parser.parse_args()
        upload_to_s3(str(args.file))

if __name__ =="__main__":
        #print('hello working')
        upload_to_s3('file')
