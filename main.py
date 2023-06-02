# Standalone presigining utility for S3 compatible storage.
# Requires boto3 lib.
# ex. usage 
# $ py main.py catpicture.png
# $ py main.py 'Releases/latest.exe'

# Import used libraries
import logging
import boto3
from botocore.exceptions import ClientError
import sys
# Setup hardcoded bucket name and object string from runtime argument
bucket_name = 'bucket'
object_name = sys.argv[1]
# Setup credentials and endpoint as strings for boto3
s3_api = 'https://api.your.object.storage'
aws_access = 'creds here'
aws_secret = 'and this'


def create_presigned_url(bucket_name, object_name, expiration=315360000):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', endpoint_url=s3_api, aws_access_key_id=aws_access, aws_secret_access_key=aws_secret)
    try:
        response = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

# Print the created presigned URL to cout
url = create_presigned_url(bucket_name, object_name)
print(url)
