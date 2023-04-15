from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class QrTextForm(FlaskForm):
    subject = StringField('Введите тему', validators=[DataRequired()])
    text = TextAreaField('Введите текст:', validators=[DataRequired()])
    submit = SubmitField('Закодировать')


class ContactForm(FlaskForm):
    first_name = StringField('Введите имя:', validators=[DataRequired()])
    last_name = StringField('Введите фамилию:', validators=[DataRequired()])
    phone = StringField('Введите номер телеффона:', validators=[DataRequired()])
    submit = SubmitField('Закодировать')



