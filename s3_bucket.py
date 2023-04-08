# Create S3 bucket using AWS CLI

import boto3

aws_resource = boto3.resource("s3")

# Name the bucket uniquely, no spaces
bucket = aws_resource.Bucket("test-bucket-onirin")

response = bucket.create(
    ACL='private', #for private bucket, change 'public-read' to 'private'
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'
    },
    
)

print(response)

# CLI command to run: python3.7 <file_name>