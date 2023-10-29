from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class UserForm(FlaskForm):
    id = StringField('N° Employee', validators=[DataRequired()])
    prefijo = RadioField('Prefix', choices=[('ET', 'ET'), ('AE', 'AE')], validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    campaign = SelectField('Campaign', choices=[('1', 'UP'), ('2', 'ATH Movil'), ('3', 'Place to Pay')], validators=[DataRequired()])
    role = SelectField('Role', choices=[('1', 'Analyst'), ('2', 'Supervisor')], validators=[DataRequired()])
