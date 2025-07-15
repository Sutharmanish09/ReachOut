# ✉️ ReachOut

A sleek, modern contact form built with **Flask** & **Python**, designed to capture user information and deliver it directly to your inbox — with style.

---

## 📝 Description

**ReachOut** is a fully responsive, dark-themed contact form solution that connects your website visitors seamlessly to your email inbox.  
With a stunning purple-gradient UI, smooth animations, and robust email integration, it’s perfect for portfolios, landing pages, or any project needing a professional contact system.

---

## 🚀 Features

✅ **Modern Dark UI** — Elegant design with floating labels & subtle transitions  
✅ **Email Notifications** — Instantly forwards submissions to your inbox  
✅ **Dual Emails** — Sends confirmation emails to users & alerts to admins  
✅ **Responsive Design** — Optimized for desktops, tablets, and mobile devices  
✅ **Graceful Error Handling** — Custom error pages with clear messaging  
✅ **Success Page** — Personalized thank-you screen after submission

---

## 🛠️ Technologies

- **Python 3.x**
- **Flask** web framework
- **SMTP** (Gmail App Password) for email delivery
- **HTML5 & CSS3** with animations
- Responsive, mobile-first design

---

## 📦 Installation

```
git clone https://github.com/Sutharmanish09/ReachOut.git
cd ReachOut
pip install flask
```

Access the form at http://127.0.0.1:5000/

---

## ⚙️ Configuration

   Open app.py

   Replace:

   "your_actual_email@gmail.com" → your Gmail address

   "your_app_password" → Gmail App Password (see below)

   "your_secret_key" → any random secret string

## 🔑 Setting Up Gmail App Password

   Enable 2-Step Verification on your Google account

   Generate an App Password:

   Google Account → Security → App Passwords

   Choose “Mail” and your device

   Copy the generated 16-character password into your config

---

## ▶️ Running the App
```
python app.py
```

Access the form at http://127.0.0.1:5000/

---

### ✏️ Usage

   Fill in your name, email, and message

   Click Send Message

   The user instantly gets a confirmation email

   The admin receives the form submission in their inbox

---

### 🔗 Integration

To use ReachOut in your existing website:

   Copy the /templates folder into your project

   Add the Flask routes (app.py) or merge them with your app

   Update email configs with your credentials

### 📄 License

Released under the MIT License.

### 📬 Contact

Questions? Feedback?
Reach me at: [manishsuthar.dev@gmail.com]


*ReachOut: Connecting people through beautiful design and reliable technology.*
