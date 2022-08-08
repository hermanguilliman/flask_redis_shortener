from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class AddUrlForm(FlaskForm):
    url = StringField('URL', validators=[
        URL(message="Bad URL. Need url like this https://my.website"),
        DataRequired(message="The URL cannot be empty")
        ])
    
    submit = SubmitField('Short it!')
