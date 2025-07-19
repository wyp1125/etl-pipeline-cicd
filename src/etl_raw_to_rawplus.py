import boto3
import botocore
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    upstream_bucket=event['upstream_bucket']
    source_bucket=event['source_bucket']
    target_bucket=event['target_bucket']
    upstream_key=event['upstream_key']
    source_key=event['source_key']
    target_key=event['target_key']
    upstream_info = {'Bucket': upstream_bucket, 'Key': upstream_key}
        
    try:
        response = s3.meta.client.copy(upstream_info, source_bucket, source_key)
        logger.info("File copied to the destination bucket successfully!")
        body={"source_path":"s3://"+source_bucket+"/"+source_key,"target_path":"s3://"+target_bucket+"/"+target_key}
        return body
        
    except botocore.exceptions.ClientError as error:
        logger.error("There was an error copying the file to the destination bucket")
        print('Error Message: {}'.format(error))
        
    except botocore.exceptions.ParamValidationError as error:
        logger.error("Missing required parameters while calling the API.")
        print('Error Message: {}'.format(error))