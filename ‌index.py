from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('update_index.html')  # Replace with your HTML file

@app.route("/send_email", methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    send_email_to_owner(name, email, message)
    return 'Message sent successfully!'

def send_email_to_owner(name, sender_email, message):
    receiver_email = "sbmonir@mun.ca"  # Replace with your email
    subject = f"New Contact from {name}"
    
    # SMTP server configuration
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port
    smtp_username = "your_smtp_username"  # Replace with your SMTP username
    smtp_password = "your_smtp_password"  # Replace with your SMTP password
    
    email_message = f"Subject: {subject}\n\nFrom: {sender_email}\nName: {name}\n\n{message}"
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, email_message)

if __name__ == "__main__":
    app.run(debug=True)
