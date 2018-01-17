import S3Copy

file = open('test.txt', 'r+')

key = file.name
bucket = 'mababio'

if S3Copy.upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'It worked!'
else:
    print 'The upload failed...'
