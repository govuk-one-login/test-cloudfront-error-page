#!/usr/bin/env python3

from __future__ import print_function
from crhelper import CfnResource

import logging
import boto3

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120, ssl_verify=None)

try:
  s3 = boto3.client('s3')
  logger.info("Created S3 client")

  with open("index.html") as f:
    logger.info("Able to open index.html")

except Exception as e:
  helper.init_failure(e)

@helper.create
@helper.update
def updateBucket(event, context):
  logger.info("Got Create or Update")
  properties = event["ResourceProperties"]
  bucket = properties["BucketName"]

  # Optionally return an ID that will be used for the resource PhysicalResourceId, 
  # if None is returned an ID will be generated.
  #
  # To add response data update the helper.Data dict
  # If poll is enabled data is placed into poll event as event['CrHelperData']

  

  s3.upload_file('index.html', bucket, 'index.html', ExtraArgs={'ContentType': 'text/html'})
    # # To return an error to cloudformation you raise an exception:
    # if not helper.Data.get("test"):
    #     raise ValueError("this error will show in the cloudformation events log and console.")
  return None

@helper.delete
def no_op(_, __):
  pass

def handler(event, context):
  helper(event, context)
