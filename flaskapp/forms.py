from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
# from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

## FORMS_REGISTER
class forms_register(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    forname = StringField('Forname')
    surname = StringField('Surname')
    submit = SubmitField('Sign up')

    """
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already taken. Try with another one.")
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("An Account with this email was already found.")
    
    def validate_tos(self, accepttos):
        if accepttos.data is False:
            raise ValidationError("You have to accept the Terms of Service to continue.")"""

## FORMS_LOGIN
class forms_login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

## FORMS_ACCOUNT_UPDATE
class forms_account_update(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(),  Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', 
                        validators=[FileAllowed(['jpg', 'png'])])
    forname = StringField('Forname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    job = StringField('Job Description')
    region = StringField('Region')
    city = StringField('City')

    """ 
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("This username is already taken. Try with another one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("An Account with this email was already found.") """