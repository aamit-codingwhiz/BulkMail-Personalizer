# BulkMail-Personalizer
# Bulk Email Sender

This is a Python-Flask web application for sending personalized bulk emails using data from a CSV file.

## Features
- Upload a CSV file with recipient information.
- Customize email content with placeholders.
- Send personalized emails to recipients.


## CSV Format
The CSV file should contain recipient data with columns such as `name`, `email`, and other fields you want to personalize.

Example CSV format:
```
name,email,company
John Doe,johndoe@example.com,Acme Inc.
Jane Smith,janesmith@example.com,Widgets Co.
```

## Email Content
Customize the email content with placeholders (e.g., `{name}`, `{company}`) that will be replaced with data from the CSV file.

## Authentication
You will need an `app password` to verify.
To create an app password for your Google Account:

    Make sure you have 2-Step Verification turned on.
    Go to your Google Account settings.
    Select Security, then 2-Step Verification.
    Scroll down and click on App passwords.
    Give the app password a name.
    Click Generate.
    Follow the on-screen instructions to use the app password in your project.
    Once done, select Done.

Remember, you usually need to do this only once for each app or device.
