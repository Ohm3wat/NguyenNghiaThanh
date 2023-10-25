from flask_wtf import FlaskForm
from wtforms import DateTimeLocalField, StringField, PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo,InputRequired

class SignUpForm(FlaskForm):
    inputFirstName=StringField('First Name',
        [DataRequired(message="Please enter your first name!")])
    inputLastName=StringField('Last Name',
        [DataRequired(message="Please enter your last name!")])
    inputEmail=StringField('Email address',
        [Email(message="Not a valid email address!"),
        DataRequired(message="Please enter your email address!")])
    inputPassword=PasswordField('Password',
        [InputRequired(message="Please enter your password!"),
        EqualTo('inputConfirmPassword',message="Password does not match!")])
    inputConfirmPassword=PasswordField('Confirm password')
    submit=SubmitField('Sign Up')

class SignInForm(FlaskForm):
    inputEmail=StringField('Email address',
                           [Email(message="Not a valid email address"),
                            DataRequired(message="Please enter your email address!")])
    inputPassword=PasswordField('Password',
                                [InputRequired(message="Please enter your password!")])
    submit=SubmitField('Sign In')

class TaskForm(FlaskForm):
    inputDescription=StringField('Task Description',
                                 [DataRequired(message="Please enter your task content!")])
    inputPriority=SelectField('Priority',coerce=int)
    submit1=SubmitField('Create Task')
    submit2=SubmitField('Edit Task')

class ProjectForm(FlaskForm):
    inputName=StringField('Project Name',
        [DataRequired(message="Please enter your project name!")])
    inputDescription=StringField('Project Description',
        [DataRequired(message="Please enter your project description!")])
    inputDeadline = DateTimeLocalField('Project Deadline', format='%Y-%m-%dT%H:%M', 
        validators=[DataRequired(message="Please select a valid deadline")])
    inputStatus=SelectField('Status', coerce=int)
    
    submit=SubmitField('Create Project')
    

