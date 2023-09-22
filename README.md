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
