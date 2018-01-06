'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: video conerter. Converts videos to web appropriate formats(.mp4, ..etc)
How: Grab video and have a docker container do the conversion and report back when it's done.
send text or email when the conversion is done.

'''


import argparse



def get_name(phone_num):
        try:
                client_obj =  client.lookups.phone_numbers("+1"+ phone_num).fetch(type="caller-name", )
        except TwilioException as e:
                        print('fun' + e)

        return client_obj.caller_name['caller_name']


def main():
        parser =  argparse.ArgumentParser()
        parser.add_argument("num", help=" 7 digit phone number", type=int)
        args = parser.parse_args()
        argument =  str(args.num)


if __name__ =="__main__":
        main()
