# Uploading files to s3 using s3cmd

## What is S3cmd

S3cmd (s3cmd) is a free command line tool and client for uploading, retrieving and managing data in Amazon S3 and other cloud storage service providers that use the S3 protocol.
It is best suited for power users who are familiar with command line programs. 
It is also ideal for batch scripts and automated backup to S3, triggered from cron, etc.

S3cmd is written in Python. It's an open source project available under GNU Public License v2 (GPLv2) and is free for both commercial and private use.

## Supported Operating Systems

We have tested s3cmd on both Linux and Mac OS, but it should work on Windows too. See https://s3tools.org/kb/item12.htm

## Install s3cmd

See https://github.com/s3tools/s3cmd/blob/master/INSTALL.md for installation instructions.

## Configure s3cmd

Because we use Scaleway Object Storage, we need to tell s3cmd to use the correct endpoint.

There are several ways to do it, and we will show a few.

## Option 1: Specify all necessary parameters with every command

```bash 
export ACCESS_KEY=<PUT YOUR_ACCESS_KEY HERE>
export SECRET_KEY=<PUT YOUR_SECRET_KEY HERE>
export BUCKET="s3://<put your bucket name here>"

s3cmd ls --access_key=$ACCESS_KEY --secret_key=$SECRET_KEY --region=fr-par --host=s3.fr-par.scw.cloud --host-bucket="%(bucket)s.s3.fr-par.scw.cloud" $BUCKET
```

### Option 2: Explicitly specify a config file for every command.

First, create a config file in your current directory:
 
```bash 
export ACCESS_KEY=<PUT YOUR_ACCESS_KEY HERE>
export SECRET_KEY=<PUT YOUR_SECRET_KEY HERE>
export BUCKET="s3://<put your bucket name here>"

echo "BUCKET=${BUCKET}"

cat << EOF > my_s3cmd.config

[default]
access_key = ${ACCESS_KEY}
secret_key = ${SECRET_KEY}
bucket_location = fr-par
host_base = s3.fr-par.scw.cloud
host_bucket = %(bucket)s.s3.fr-par.scw.cloud
EOF
```

Now, access the bucket using s3cmd:
```bash
s3cmd --config=my_s3cmd.config ls ${BUCKET}/input
```

### Option 3: Create a config file in the default location (~/.s3cfg)

> **Note**                                                  
This method will save your secret key in a (hidden) file in your home directory.
                                               
```bash
export ACCESS_KEY=SCWxxxxxxxxxxxxxxxxx
export SECRET_KEY=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee 
export BUCKET=s3://tld-xx-laughing-panda-xx/

s3cmd --configure \
--host-bucket='%(bucket)s.s3.fr-par.scw.cloud' \
--host=s3.fr-par.scw.cloud \
--region=fr-par \
--access_key=${ACCESS_KEY} \
--secret_key=${SECRET_KEY} \
${BUCKET}
```         
                    
On our machine, we had to confirm these questions:
* Access key 
* Secret key 
* Default region
* S3 Endpoint 
* DNS-style bucket+hostname:port template for accessing a bucket
* Encryption password:
* Path to GPG program [None]:
* Use HTTPS protocol [Yes]:
* HTTP Proxy server name:
* Test access with supplied credentials? [Y/n] 

And finally, enter "y" when asked to Save settings? [y/N]
                       
You should now be able to consult the content of your bucket and add files to the input folder:

```bash
s3cmd ls $BUCKET/
s3cmd put sample.csv $BUCKET/input/sample.csv
```

