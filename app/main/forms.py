from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField, BooleanField, DateField


 

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
    vote=RadioField('default field arguments', choices=[('1', 'Like'), ('1', 'Dislike')])
    submit = SubmitField('SUBMIT') 

class UpvoteForm(FlaskForm):
    submit = SubmitField('Upvote')


class SubscriptionForm(FlaskForm):
    email = StringField('Email Address',validators=[Required()])
    submit = SubmitField('Subscribe!')
    