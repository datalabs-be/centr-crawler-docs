# Uploading files using the Python boto3 library
             
boto3 is a Python library provided by Amazon Web Services (AWS) that makes it easy to access S3 buckets (and other AWS Services).
                                      
Since ScaleWay Object Storage is compatible with S3, we can use boto3 to upload and download files to/from our bucket.

## References
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

## Install boto3

We recommend using a virtual environment to install boto3.
```
python3 -m venv venv
source venv/bin/activate
pip install boto3
```

## Upload a file

```python

import boto3

```




