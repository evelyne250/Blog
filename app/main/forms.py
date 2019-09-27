from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

class PostForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("Pitch Now :",validators=[Required()])
	category = StringField('Category', validators=[Required()])
	submit = SubmitField('Submit')

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')