from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this_in_production'

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data with validation
        name = request.form.get('name', '').strip()
        user_email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not name or not user_email or not message:
            return render_template('error.html', error="All fields are required")
        
        # Email configuration
        sender_email = "your_email@gmail.com"
        app_password = "app_password"
       
        print(f"Attempting to send email from {sender_email} to {user_email}")
        
        # Create message for user
        user_msg = MIMEMultipart()
        user_msg['From'] = sender_email
        user_msg['To'] = user_email
        user_msg['Subject'] = "Thank you for your submission"
        
        user_body = f"""Dear {name},

Thank you for your submission. We have received the following message:

{message}

We will get back to you soon.

Best regards,
Your Team"""
        
        user_msg.attach(MIMEText(user_body, 'plain'))
        
        # Create admin notification message
        admin_msg = MIMEMultipart()
        admin_msg['From'] = sender_email
        admin_msg['To'] = sender_email
        admin_msg['Subject'] = f"New Form Submission from {name}"
        
        admin_body = f"""New submission details:

Name: {name}
Email: {user_email}
Message: {message}"""
        
        admin_msg.attach(MIMEText(admin_body, 'plain'))
        
        # Connect to Gmail SMTP server
        print("Connecting to SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("Logging in...")
        server.login(sender_email, app_password)
        
        # Send email to user
        print(f"Sending email to user: {user_email}")
        server.sendmail(sender_email, [user_email], user_msg.as_string())
        
        # Send admin notification
        print(f"Sending admin notification to: {sender_email}")
        server.sendmail(sender_email, [sender_email], admin_msg.as_string())
        
        server.quit()
        print("Emails sent successfully!")
        
        return render_template('success.html', name=name)
        
    except smtplib.SMTPAuthenticationError as e:
        error_msg = "Authentication failed. Please check your email and app password."
        print(f"SMTP Auth Error: {e}")
        return render_template('error.html', error=error_msg)
    
    except smtplib.SMTPRecipientsRefused as e:
        error_msg = f"Invalid recipient email address: {user_email}"
        print(f"Recipients Refused: {e}")
        return render_template('error.html', error=error_msg)
    
    except smtplib.SMTPException as e:
        error_msg = f"SMTP error occurred: {str(e)}"
        print(f"SMTP Error: {e}")
        return render_template('error.html', error=error_msg)
    
    except Exception as e:
        error_msg = f"An unexpected error occurred: {str(e)}"
        print(f"General Error: {e}")
        return render_template('error.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)