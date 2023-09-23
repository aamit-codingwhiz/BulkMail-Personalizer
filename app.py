import yagmail
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_emails', methods=['POST'])
def send_emails():
    if 'csv_file' not in request.files:
        return redirect(url_for('index'))

    csv_file = request.files['csv_file']
    if csv_file.filename == '':
        return redirect(url_for('index'))

    sender_mail_address = request.form['sender_mail_address']
    sender_mail_password = request.form['sender_mail_password']
    email_content = request.form['email_content']

    try:
        df = pd.read_csv(csv_file)

        for index, row in df.iterrows():
            recipient_email = row['email']
            personalized_content = email_content

            for column_name, column_value in row.items():
                placeholder = f'{{{column_name}}}'
                if placeholder in personalized_content:
                    personalized_content = personalized_content.replace(
                        placeholder, str(column_value))

            send_email(sender_mail_address, sender_mail_password,
                       recipient_email, 'Your Subject', personalized_content)

        return 'Emails sent successfully!'
    except Exception as e:
        return f'Error: {str(e)}'


def send_email(sender_mail_address, sender_mail_password, recipient_email, subject, body):
    try:
        your_email = sender_mail_address
        your_password = sender_mail_password
        yag = yagmail.SMTP(your_email, your_password)

        yag.send(
            to=recipient_email,
            subject=subject,
            contents=body
        )

        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {str(e)}")

    # Example usage:
    # send_email('recipient@example.com', 'Your Subject', 'Your Email Body')


if __name__ == '__main__':
    app.run(debug=True)
