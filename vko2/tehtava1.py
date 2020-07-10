#  GET AND WRITE JSON DATA

import requests

#  Getting JSON data
r = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data = r.json()
lista = []

def get_and_write_data(jsondata, file):
    #  Adding parameters to list
    for items in jsondata['items']:
        lista.append(items['parameter'])

    #  Joining list
    parameters = '\n'.join(lista)

    # Adding parameters to textfile
    with open(file, 'w') as tiedosto:
        tiedosto.write(parameters)

get_and_write_data(data, 'checkpoint.txt')


import logging
import boto3
from botocore.exceptions import ClientError

#CREATE BUCKET

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

create_bucket('kati-checkpoint2-bucket', 'eu-west-2')

# UPLOAD FILE TO BUCKET

def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file('checkpoint.txt', 'kati-checkpoint2-bucket')

