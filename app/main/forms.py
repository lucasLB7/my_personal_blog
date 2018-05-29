from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField, BooleanField, DateField, ValidationError
from ..models import Subscriber


 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('SUBMIT') 

class PostForm(FlaskForm):
    category_id = SelectField('Tutorial categories', choices=[('1', 'Introduction to Blender'), ('2', 'More advanced tutorials'), ('3', 'Hardcore Blender Tutorials'),('4','Blender python scrypting')])
    title = StringField('title',validators=[Required()])
    description = StringField('description',validators=[Required()])
    date = DateField('Start Date', format='%m/%d/%Y',validators=[Required()])
    content = TextAreaField('Write a post')
    conscent = BooleanField('I understand the regulations of posting',validators=[Required()])
    submit = SubmitField('Submit post')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on this pitch:', validators=[Required()])
    username = StringField('Whats your name.', validators=[Required()])
    submit = SubmitField('SUBMIT') 



class SubscriptionForm(FlaskForm):
    email = StringField('Email Address',validators=[Required()])
    submit = SubmitField('Subscribe!')

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email address already registered')

    