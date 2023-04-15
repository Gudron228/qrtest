from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class QrTextForm(FlaskForm):
    subject = StringField('Введите тему', validators=[DataRequired()])
    text = TextAreaField('Введите текст:', validators=[DataRequired()])
    submit = SubmitField('Закодировать')


class ContactForm(FlaskForm):
    first_name = StringField('Введите имя:', validators=[DataRequired()])
    last_name = StringField('Введите фамилию:', validators=[DataRequired()])
    phone = StringField('Введите номер телефона:', validators=[DataRequired()])
    org = StringField('Введите название организации:', validators=[DataRequired()])
    email = EmailField('Введите email:', validators=[DataRequired()])
    url = StringField('Введите url сайта:', validators=[DataRequired()])
    submit = SubmitField('Закодировать')


class ServiceForm(FlaskForm):
    service = StringField('Введите название услуги:', validators=[DataRequired()])
    food = StringField('Введите название блюда', validators=[DataRequired()])
    price = IntegerField('Введите цену блюда', validators=[DataRequired()])
    submit = SubmitField('Закодировать')



