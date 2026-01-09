import argparse
import os
from pathlib import Path

import boto3

# Sample python script to upload a file to a bucket and retrieve a list of files in a bucket
# Only provided for demonstration purposes.

def list_files(s3, bucket_name, prefix=''):
    print(f"Retrieving all files in s3://{bucket_name}/{prefix}")
    object_list = s3.list_objects(Bucket=bucket_name, Prefix=prefix)
    for obj in object_list['Contents']:
        print(f"In bucket '{bucket_name}' we found object with key = '{obj['Key']}' having a size of {obj['Size']} bytes")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket_name', type=str, required=True)
    parser.add_argument('--access-key-id', type=str, required=True)
    parser.add_argument('--secret-key', type=str, required=True)
    parser.add_argument('--download_output', type=bool, required=False, default=False)

    parsed_args = parser.parse_args()
    bucket_name = parsed_args.bucket_name
    download_output = parsed_args.download_output

    # boto3 expects these environment variables to be set
    # Or, if you have the AWS CLI installed, you could run `aws configure` instead.

    os.environ['AWS_ACCESS_KEY_ID'] = parsed_args.access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = parsed_args.secret_key

    print(f"Bucket name: {bucket_name}")
    print(f"Access key ID: {os.environ['AWS_ACCESS_KEY_ID']}")
    print(f"Secret key: {os.environ['AWS_SECRET_ACCESS_KEY']}")

    s3_endpoint_url = 'https://s3.fr-par.scw.cloud'
    s3 = boto3.client('s3', endpoint_url=s3_endpoint_url, region_name='fr-par')

    file_path='sample.csv'
    key = 'input/sample.csv'

    print(f"Uploading {file_path} to s3://{bucket_name}/{key}")
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key=key)

    list_files(s3, bucket_name, 'input/')

    print("Now delete the uploaded file")
    s3.delete_object(Bucket=bucket_name, Key=key)

    list_files(s3, bucket_name, prefix='input/')

    print(f"Retrieving all files in s3://{bucket_name}/output/")
    list_files(s3, bucket_name, prefix='output/')

    if download_output:
        object_list = s3.list_objects(Bucket=bucket_name, Prefix='output')
        for obj in object_list['Contents']:
            print(f"In bucket '{bucket_name}' we found object with key = '{obj['Key']}' having a size of {obj['Size']} bytes")
            key = obj['Key']
            path = os.path.join('downloaded_files', key)
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            print(f"Downloading {key} to {path}")
            s3.download_file(bucket_name, key, path)
    else:
        print("Skipping download. Add `--download_output` to download the files from the output folder.")