# Monthly Sample

If your zone has less than 50.000 registered domain names, you can upload all the domain names of your zone.
Otherwise, you should take a random sample of 50.000 domain names.

It is advised to generate a fresh random sample every month, considering only active registrations.

# Requirements

The file you upload should meet the following requirements:

* The file should not have a header.
* The file should have one line per domain name.
* Each line should contain one domain name including the TLD (but no trailing dot).
* The file should be encoded in UTF-8.
* The file should not contain any blank lines.
* The file should not contain any comment lines.
* The file should not exceed 5 MB.
* The file should have a '.csv' extension.
* Some valid file names
  * sample.csv
  * domain_names_for_xx.csv
  * zone_sample_january_2026_xx.csv
* We suggest you do NOT use spaces or special characters in the file name.
* Domain names that do not match your TLD will be ignored.
* Duplicate domain names will be ignored.

> **Note:**
> ⚠️ The sample has to be uploaded to the **input** folder of your bucket. ⚠️

If you get an access denied error message, it's probably because your trying to upload to the root of the bucket.

So, you should do something like this:
```
aws s3 cp sample-fr-2026-05.csv s3://mercator-data-fr/input/sample-fr-2026-05.csv
```

Or the equivalent if you're using Python or another tool.

You are allowed to spread your domain names over multiple files, but we don't see a good reason to do so. 

# Signaling that you are done uploading

Once you have uploaded your csv file. you should upload another file to indicate that we can start processing your domain names.
To do this, upload an empty file with the name 'upload_done' to the input folder of your bucket.

With the AWS CLI that could be done like this:
```bash
touch upload_done
aws s3 cp upload_done s3://mercator-data-fr/input/upload_done
```

Remember to replace 'fr' with your TLD.

If you prefer to add a short greeting to this file, feel free to do so (it will probably go unnoticed 😉).

# The results

When all the domains in your sample have been crawled, you can find the crawling result in the output folder of your bucket.

The output folder will have the following subfolders:
* tls
* dns
* web
* screenshots

More subfolders might be added in the future.

The data in the tls, dns and web folders is in parquet format and will be partitioned by year and month.
The websites linked to approximately 5% of the domain names in your sample will be visited with a browser, and the resulting HTML and screenshot will be saved in the 'screenshots' folder.  

> **Note:** The screenshots are only saved if the website is reachable.

> **Note:**
> ⚠️ The data in the output folder will be deleted after 30 days. ⚠️


