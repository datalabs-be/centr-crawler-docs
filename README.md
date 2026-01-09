# CENTR Crawler Documentation
                           
This repository contains documentation for CENTR who members participating in the monthly crawling of (a sample of) 
their zone file.
                       
# Summary

Here is an overview of the steps needed to particiapte in the monthly crawling:
* Enter your e-mail address at https://portal.datalabs.be/register
* Click the activation link in the mail you should have received.
* Choose a password. 
* Login with your password and the one-time token sent to you via email.
* Wait for confirmation that your account has been assigned to your TLD. 
* Log in to the portal and generate an access key.
* Use the access key to upload your sample to the S3 bucket for your TLD.
* Add an 'upload_done' file to signal that you are done uploading.
* Sit back and relax ☺️, the crawling results will be available soon.

See [the monthly sample](docs/monthly_sample.md) for more details about the monthly sample.

# Create an account
  
First, you need to create a user account.

Go to https://portal.datalabs.be/register and enter your email address.

> [!NOTE]   
> Make sure to use an e-mail address that uses the **domain name of your registry**.
> Otherwise you will see this error message:
> ```
> Email is not valid. Please contact someone at Data Labs if you think this is incorrect.
> ```

> [!NOTE]  
> 
> You can only register one account per email address.
> 
> But there can be multiple people at your registry, each with their own account (and access keys).

# Click the activation link
                                      
You should now receive an e-mail with an activation link.
The mail is sent by `no-reply@datalabs.be` and should have a correct DKIM signature.
Please let us know if the mail landed in your spam folder or if you did not receive the mail.

When you click the activation link, you will be asked to fill in your first and last name and choose a strong password.

# You will be redirected to the login form:

After you enter your credentials, you will receive a one-time token via e-mail.
Copy-paste the token in the form and click `Verify`.

> [!TIP]
> Now, you can delete the e-mails with the activation link and the one-time token.
>
> Every time you log in, you will need
> * your email address
> * your password
> * A fresh one-time token that you will receive via e-mail.

# Home page

Once authenticated, you will be redirected to the home page.

At this moment, you cannot yet request access keys.
First, we must assign your user account to the correct TLD.

We will try to assign your account to a TLD within 48 hours after activating your account.
Please contact maarten[at]bosteels[.]eu if you have not received a confirmation within this time.

# Requesting access keys

Once you received confirmation that your account was linked to your TLD, you can go to the home page
and request access keys.

Select the TLD and click `Request access keys`.

# Safely store your access key
                                                                   
You will now see the newly created key.
Each access key consists of an access key ID and a secret key.

> [!WARNING]                    
> Safely store the access key ID and the secret key. The secret key will be shown only once!

If you failed to store the key, just delete the key and request a new one.

To allow for safely rotating keys, you can create up to three access keys per TLD.

> [!IMPORTANT]                                           
Please note that access keys automatically expire one year after creation.

# Uploading a sample of your zone file

Every month you should upload a random sample of your zone file to the S3 bucket for your TLD.
The sample should be in CSV format with no headers and one column: the domain name including the TLD. 
The CSV file should contain no more than 50.000 records and have a '.csv' extension.

To upload a sample of your zone file, you need this information:

* Your access key ID
* Your secret key
* The name of the S3 bucket for your TLD

You can find this information on the home page.

You have several options to upload a sample of your zone file:
* Use the command line tool `s3cmd`
* Use the AWS SDK for your preferred programming language
* Use a tool with a graphical user interface, like [Cyberduck](https://cyberduck.io/)
* and many more.

We will describe some of these options in the next sections.
* [Upload with s3cmd](docs/upload_with_s3cmd.md)
* [Upload using Python and boto3](docs/upload_with_python.md)
                             
More details about the monthly sample can be found [here](docs/monthly_sample.md).


