export ACCESS_KEY=$1
export SECRET_KEY=$2
export BUCKET=$3

echo "BUCKET=${BUCKET}"

cat << EOF > my_s3cmd.config

[default]
access_key = ${ACCESS_KEY}
secret_key = ${SECRET_KEY}
bucket_location = fr-par
host_base = s3.fr-par.scw.cloud
host_bucket = %(bucket)s.s3.fr-par.scw.cloud
EOF

s3cmd --config=my_s3cmd.config ls ${BUCKET}
s3cmd --config=my_s3cmd.config ls ${BUCKET}/input

echo "abc.be" > sample.csv

cat << EOF > sample.csv
dnsbelgium.be
google.be
example.be
a-lot-more-domains-from-your-tld.be
EOF

cat sample.csv

s3cmd --config=my_s3cmd.config put sample.csv ${BUCKET}/input/sample.csv
s3cmd --config=my_s3cmd.config ls ${BUCKET}/input/

# To indicate that you are done uploading

#touch upload_done
#s3cmd put upload_done ${BUCKET}/input/upload_done

echo "After uploading the upload_done file:"

s3cmd --config=my_s3cmd.config ls ${BUCKET}/input/