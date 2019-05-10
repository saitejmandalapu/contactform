from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('name')])
    email = StringField('E-mail', validators=[DataRequired('E-mail '),Email('email ')])
    subject = StringField('subject', validators=[DataRequired('subject')])
    message = TextAreaField('Message', validators=[DataRequired('message')])
    submit = SubmitField("send")