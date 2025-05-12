from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user_email = request.form['email']  # This is the email entered by the user in the form
    message = request.form['message']
    
    # Email configuration
    sender_email = "your_actual_mail@gmail.com"  # Replace with your actual Gmail     
    app_password = "password"  # Replace with your App Password
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email  # Send to the email address provided in the form
    msg['Subject'] = "Thank you for your submission"
    
    # Email body for the user
    user_body = f"Dear {name},\n\nThank you for your submission. We have received the following message:\n\n{message}\n\nWe will get back to you soon.\n\nBest regards,\nYour Team"
    msg.attach(MIMEText(user_body, 'plain'))
    
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        
        # Send email to the user
        text = msg.as_string()
        server.sendmail(sender_email, user_email, text)
        
        # Also send a notification to yourself (optional)
        admin_msg = MIMEMultipart()
        admin_msg['From'] = sender_email
        admin_msg['To'] = sender_email
        admin_msg['Subject'] = f"New Form Submission from {name}"
        
        admin_body = f"New submission details:\nName: {name}\nEmail: {user_email}\nMessage: {message}"
        admin_msg.attach(MIMEText(admin_body, 'plain'))
        
        server.sendmail(sender_email, sender_email, admin_msg.as_string())
        
        server.quit()
        
        # Return success page
        return render_template('success.html', name=name)
    except Exception as e:
        # Return error message
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)