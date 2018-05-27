from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField

 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('SUBMIT') 

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Creative Ideas'), ('2', 'Funny Stories'), ('3', 'Motivational Speeches'),('4','Business Ideas')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on this pitch:', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'Like'), ('1', 'Dislike')])
    submit = SubmitField('SUBMIT') 

class UpvoteForm(FlaskForm):

    submit = SubmitField('Upvote')
    