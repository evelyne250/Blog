from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

class PostForm(FlaskForm):
	author = StringField('Author', validators=[Required()])
	description = TextAreaField("Post a Blog Now :",validators=[Required()])
	category = StringField('Category', validators=[Required()])
	submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
	author = StringField('Author', validators=[Required()])
	description = TextAreaField("Edit your Blog Now :",validators=[Required()])
	category = StringField('Category', validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()


class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')