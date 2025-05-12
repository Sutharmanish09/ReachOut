# ReachOut

A sleek, modern contact form built with Flask and Python that collects user information and delivers it directly to your email inbox.

## Description

ReachOut is an elegant, dark-themed contact form solution that seamlessly connects your website visitors with your inbox. Built with Flask and featuring a beautiful purple-gradient UI, this project demonstrates how to create a professional-grade contact system with email integration.

## Features

- **Stunning Dark UI** - Modern, animated interface with floating labels and smooth transitions
- **Email Integration** - Automatically forwards form submissions to your inbox
- **Dual Notifications** - Sends confirmation emails to users and notification emails to administrators
- **Responsive Design** - Works beautifully across desktop and mobile devices
- **Error Handling** - Elegant error pages with helpful information
- **Success Confirmation** - Custom success page with personalized acknowledgment

## Technologies Used

- Python 3.x
- Flask web framework
- SMTP email integration
- HTML5 / CSS3
- Responsive design with animations

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Sutharmanish09/ReachOut.git
   cd ReachOut
   ```

2. Install required packages:
   ```bash
   pip install flask
   ```

3. Configure the app.py file with your email credentials:
   - Replace `"your_actual_email@gmail.com"` with your Gmail address
   - Replace `"your_app_password"` with your Gmail App Password
   - Replace `"your_secret_key"` with a random string for security

## Setting Up Gmail App Password

1. Enable 2-Step Verification on your Google account
2. Generate an App Password:
   - Go to your Google Account → Security → App passwords
   - Select "Mail" and your device
   - Use the generated 16-character password in the app configuration

## Running the Application

```bash
python app.py
```

Access the form at http://127.0.0.1:5000/

## How to Use

1. Fill out the form with name, email, and message
2. Click "Send Message"
3. The user receives a confirmation email
4. You receive all form submissions in your inbox

## Integration

To integrate this form into your existing website:
1. Copy the templates folder to your project
2. Add the Flask routes to your application
3. Update the email configuration with your credentials

## License

[MIT License](LICENSE)

## Contact

For questions or support, please reach out at [your-email@example.com]

---

*ReachOut: Connecting people through beautiful design and reliable technology.*
