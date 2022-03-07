from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EbookForm(FlaskForm):
    title = StringField('EBook title', id='ebook_title')
    author_last_name = StringField('Author last name', id='ebook_author_last_name')
    submit = SubmitField('Save', id='ebook_submit')
