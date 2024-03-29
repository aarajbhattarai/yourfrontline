from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm, CSRFProtect
from flask_mail import Mail, Message
import secrets
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

application = Flask(__name__)

application.config['SECRET_KEY'] = secrets.token_urlsafe(16)
csrf = CSRFProtect(application)

mail = Mail(application)
application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
MAIL_DEFAULT_SENDER = 'aarajbhattarai11@gmail.com'
application.config['MAIL_USERNAME'] = 'aarajbhattarai11@gmail.com'
application.config['MAIL_PASSWORD'] = '#9851CLFA58A0D8183629r'
application.config['MAIL_DEFAULT_SENDER'] = 'aarajbhattarai11@gmail.com'
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
mail = Mail(application)

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    address = StringField("Address", validators=[DataRequired()])
    number = StringField("Number", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

@application.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form['name']
        message = request.form['message']
        email = request.form['email']
        address = request.form['address']
        number = request.form['number']
        msg = Message('Frontline Query', recipients=['aarajbhattarai@gmail.com','metallicanup@gmail.com','yudeep@gmail.com'])
        msg.body = ("Name:{0}\n"
                    "\nEmail:{1}"
                    "\n Number:{2}"
                    "\n Message:{3}".format(name, email, number, message, ))
        mail.send(msg)
        return render_template('index.html', success=True)

    else:

        return render_template('index.html', form=form)


if __name__ == '__main__':
    application.run()
