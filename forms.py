'''
author: WangQuanyi
date: 2019-11-21 10:28
name: forms.py
contact: wang0759@algonquinlive.com

'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

# search student by first name
class inputForm(FlaskForm):
    lstNames = SelectField('Student First Name')
    Search = SubmitField('Search')


