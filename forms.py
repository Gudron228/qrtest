from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class QrTextForm(FlaskForm):
    text = TextAreaField('Введите текст:', validators=[DataRequired()])
    submit = SubmitField('Закодировать')



