from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateTimeField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class CreateStadiumForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

class CreateMatchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    stadium_id = IntegerField('Stadium ID', validators=[DataRequired()])
    start_at = DateTimeField('Start At', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
