import argparse

def main():
        parser =  argparse.ArgumentParser()
        parser.add_argument("num", help=" 7 digit phone number", type=int)
        args = parser.parse_args()

        # Your Account Sid and Auth Token from twilio.com/user/account
        account_sid = ""
        auth_token = ""

        client = Client(account_sid, auth_token)

        val  ='' get_name(str(args.num))
        print(val)

if __name__ =="__main__":
        #print('hello working')
        main()
