from flask_wtf import FlaskForm     #flaskform for creating form
from wtforms import StringField, PasswordFiled ,SubmitField, BooleanFiled   #BooleanField for true/false as in RememberMe checkbox
from wtforms.validators import DataRequired, Length, Email, EqualTo  #various validaters for sanatising user input, like equalto for making confirmpass=pass 

class RegistrationForm(FlaskForm):
	username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('email', validators=[DataRequired(), Email()])
	password = PasswordFiled('password', validators=[DataRequired()]) 
	confirm_password = PasswordFiled('password', validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('email', validators=[DataRequired(), Email()])
	password = PasswordFiled('password', validators=[DataRequired()]) 
	Remember = BooleanField('Remembering Me')
	submit = SubmitField('Log In')
