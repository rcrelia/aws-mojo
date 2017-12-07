from __future__ import print_function
import os
import json
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

print('Loading function... cold start initialization window')

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print('Loading function... main function handler starting')
    bucket_name = os.environ['bucket_name']
    bucket_key = os.environ['bucket_key']
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)

    put_object_into_s3(bucket_name, bucket_key, message)
    get_object_from_s3(bucket_name, bucket_key)

def put_object_into_s3(bucket_name, bucket_key, message):
    try:
        # Define subsegments manually
        xray_recorder.begin_subsegment('put_object')
        response = s3_client.put_object(Bucket=bucket_name, Key=bucket_key, Body=message)
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        xray_recorder.current_subsegment().put_annotation('put_response', status_code)
    finally:
        xray_recorder.end_subsegment()

@xray_recorder.capture('get_object')
def get_object_from_s3(bucket_name, bucket_key):
    # Use decorators to automatically set the subsegments
    response = s3_client.get_object(Bucket=bucket_name, Key=bucket_key)
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    xray_recorder.current_subsegment().put_annotation('get_response', status_code)
