#  DOWNLOAD FILE FROM S3 BUCKET
import os.path
import time
import boto3
import argparse

parser = argparse.ArgumentParser(description='Give lines to print.')
parser.add_argument('integer', type=int)

lines = parser.parse_args()
lines = lines.integer

s3 = boto3.client('s3')
s3.download_file('kati-checkpoint2-bucket', 'checkpoint.txt', 'checkpoint2.txt')

#  PRINT LINES


file_path = 'checkpoint2.txt'

while not os.path.exists(file_path):
    time.sleep(1)

if os.path.isfile(file_path):
    with open(file_path) as tiedosto:
        for i in tiedosto.readlines():
            if lines == 0:
                break
            print(i)
            lines = lines - 1

else:
    raise ValueError("%s isn't a file!" % file_path)