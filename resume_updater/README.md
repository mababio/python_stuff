# Resume Updater

I put together a tool that will automatically update my resume hosted on AWS S3 platform with the local copy of my resume.

Tech stack:
-  Python3
- boto3 python module
- when-changed(https://github.com/joh/when-changed) python module
- Unix ampersand background processor

[Installation]

- Make sure you have your S3 config file setup https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html
- Make sure you put your twilio creds in the config.ini file
- ``` git clone https://github.com/mababio/python_stuff.git ```
- Navigate to resume_updater directory
- ``` python3 setup.py install ```
- ``` pip3 install https://github.com/joh/when-changed/archive/master.zip ```
- Run this  ``` when-changed [FILE_Trigger] -c 'resume_updater [FILE_TO_Upload]' & ```
