# Python example

This folder contains a sample python script that can 

* upload a file to a bucket 
* retrieve a list of files in a bucket
* download the files from a given bucket and prefix 

# Using uv 

```
cd python
uv sync 
uv add boto3
uv run upload_file.py --bucket_name 'your-bucket' --access-key-id 'SCWxxxxx' --secret-key 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee' --download_output True
```

# Using pip
```
python3 -m venv venv
source venv/bin/activate
pip install boto3   
python upload_file.py --bucket_name 'your-bucket' --access-key-id 'SCWxxxxx' --secret-key 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee' --download_output True
```