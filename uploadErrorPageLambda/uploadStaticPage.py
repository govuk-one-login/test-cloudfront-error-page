#!/usr/bin/env python3
import os
import boto3
import cfnresponse

def handler(event, context):
  s3=boto3.client('s3')

  bucket = os.environ.get('BucketName')

  try:
    with open ("static-error-pages/index.html") as f:
      responseData = {}
      responseData['Data'] = s3.upload_fileobj(f, bucket, "cloudfront")
      cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
  except:
    cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
