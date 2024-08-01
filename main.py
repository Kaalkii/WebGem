from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'Gulambi'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'varun.ranjan49@gmail.com'  # Replace with your SMTP username
app.config['MAIL_PASSWORD'] = 'fptu hoii wrra dxnn'  # Replace with your SMTP password
app.config['MAIL_DEFAULT_SENDER'] = ('Gulambi', 'varun.ranjan9089@gmail.com')  # Replace with your name and email

mail = Mail(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject, recipients=['varun.ranjan49@gmail.com'])  # Replace with the recipient's email address
    msg.body = f"From: {name} <{email}>\n\n{message}"

    try:
        mail.send(msg)
        return 'OK'  # Ensure the response is exactly 'OK'
    except Exception as e:
        return str(e), 500  # Return error message and status code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
