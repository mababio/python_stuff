'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: video conerter. Converts videos to web appropriate formats(.mp4, ..etc)
How: Grab video and have a docker container do the conversion and report back when it's done.
send text or email when the conversion is done.

'''

import argparse
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from config import config


def main():
    #Getting cmd_line args
    parser =  argparse.ArgumentParser()
    parser.add_argument("file", help="file path", type=str)
    args = parser.parse_args()
    print(str(args.file))

if __name__ =="__main__":
    main()
