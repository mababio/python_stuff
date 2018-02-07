"""
Author: Michael Ababio
Date: 02-06-2017
Purpose: centralize point for python tool
"""

import argparse
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
from config import config



def main():
    """
    main function
    """
    # Getting cmd_line args
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file path", type=str)
    args = parser.parse_args()
    print(str(args.file))
    # Example usage of config
    print(config.ACCOUNT_SID)

if __name__ == "__main__":
    main()
