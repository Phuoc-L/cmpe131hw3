from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

'''
The form for when a user write a message

data
------
author : String
    The name of the user who is giong to write the message
message : String
    The message that the user want to post
'''
class MessageForm(FlaskForm):
    # add
    # author (string) validator should make this textbox required
    author = StringField('author', validators=[DataRequired()])
    # message (string) validator should make this textbox required
    message = StringField('message', validators=[DataRequired()])
    # submit (button) text should say 'Send'
    submit = SubmitField('Send')