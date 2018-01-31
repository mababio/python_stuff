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
