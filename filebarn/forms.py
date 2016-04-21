from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Email, Length


class LoginForm(Form):
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
