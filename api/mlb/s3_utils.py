import boto3
import logging
import os

# Read the list of existing buckets
def list_buckets():
    """
    List all the buckets in the account.
    """
    try:
        s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        response = s3.list_buckets()
        if response:
            for bucket in response['Buckets']:
                print(f'Bucket: {bucket["Name"]}')

    except Exception as e:
        logging.error(e)
        return False
    return True

# Upload a file to S3
def upload_to_s3(file_path, bucket_name, object_name):
    """
    Upload a file to an S3 bucket.

    Args:
        file_path (str): The path to the file to upload.
        bucket_name (str): The name of the bucket.
        object_name (str): The name of the object in the bucket.

    Returns:
        bool: True if the file was uploaded successfully, otherwise False.
    """
    try:
        s3 = boto3.client('s3')
        s3.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True

# Delete file from S3
def delete_from_s3(bucket, key_name):
    """
    Delete a file from an S3 bucket.

    Args:
        bucket (str): The name of the bucket.
        key_name (str): The name of the object in the bucket.

    Returns:
        bool: True if the file was deleted successfully, otherwise False.
    """
    s3 = boto3.client('s3')
    try:
        s3.delete_object(Bucket=bucket, Key=key_name)
    except Exception as e:
        logging.error(e)
        return False
    return True

# Get all objects in a bucket
def get_all_objects(bucket):
    """
    Get a list of objects in an S3 bucket.

    Args:
        bucket (str): The name of the bucket.

    Returns:
        list: A list of objects in the bucket.
    """
    try:
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=bucket)
        if response:
            return response['Contents']
    except Exception as e:
        logging.error(e)
        return None

# Get an object from a bucket
def get_object(bucket, key):
    """
    Get an object from an S3 bucket.

    Args:
        bucket (str): The name of the bucket.
        key (str): The name of the object in the bucket.

    Returns:
        dict: The object data.
    """
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        if response:
            return response['Body'].read()
    except Exception as e:
        logging.error(e)
        return False

# Download an object from a bucket
def download_object(bucket, key, file_path):
    """
    Download an object from an S3 bucket.

    Args:
        bucket (str): The name of the bucket.
        key (str): The name of the object in the bucket.
        file_path (str): The path to save the downloaded object.

    Returns:
        bool: True if the object was downloaded successfully, otherwise False.
    """
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket, key, file_path)
    except Exception as e:
        logging.error(e)
        return False
    return True

