from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateBookForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    num_pages = IntegerField('Pages', validators=[DataRequired()])
    pub_id = IntegerField('PublisherID', validators=[DataRequired()])
    submit = SubmitField('Create')
