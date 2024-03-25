import yagmail
from flask import Flask, flash, render_template, request, redirect, url_for
import pandas as pd
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_emails', methods=['POST'])
def send_emails():
    if 'csv_file' not in request.files:
        return redirect(url_for('index'))

    csv_file = request.files['csv_file']
    if csv_file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if csv_file and allowed_file(csv_file.filename):
        filename = secure_filename(csv_file.filename)
        csv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        csv_file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(f"Success saving file. Location: {os.path.join(app.config['UPLOAD_FOLDER'], filename)}")

    sender_mail_address = request.form['sender_mail_address']
    sender_mail_password = request.form['sender_mail_password']
    email_subject = request.form['email_subject']
    email_content = request.form['email_content']
    email_attachments = request.files['attachments']

    save_location = os.path.join(app.config['UPLOAD_FOLDER'], email_attachments.filename)
    email_attachments.save(save_location)
    email_attachments = save_location
    print(type(save_location))

    try:
        df = pd.read_csv(csv_file_location)

        for index, row in df.iterrows():
            recipient_email = row['email']
            personalized_content = email_content
            personalized_subject = email_subject

            for column_name, column_value in row.items():
                placeholder = f'{{{column_name}}}'
                
                if placeholder in personalized_content:
                    personalized_content = personalized_content.replace(
                        placeholder, str(column_value))
                
                if placeholder in personalized_subject:
                    personalized_subject = personalized_subject.replace(
                        placeholder, str(column_value))

            send_email(
                sender_mail_address=sender_mail_address, 
                sender_mail_password=sender_mail_password,
                recipient_email=recipient_email, 
                subject=personalized_subject, 
                body=personalized_content, 
                attachments=email_attachments
            )

        return 'Emails sent successfully!'
    except Exception as e:
        return f'Error: {str(e)}'


def send_email(sender_mail_address, sender_mail_password, recipient_email, subject, body, attachments=None):
    try:
        your_email = sender_mail_address
        your_password = sender_mail_password
        yag = yagmail.SMTP(your_email, your_password)

        yag.send(
            to=recipient_email,
            subject=subject,
            contents=body,
            attachments=[attachments]
        )

        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)