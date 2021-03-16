from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email



class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = StringField('No. of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    types = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'Images Only'])])
