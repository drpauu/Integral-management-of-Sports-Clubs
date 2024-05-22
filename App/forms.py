from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email

class MembreForm(FlaskForm):
    num_soci = StringField('Num Soci', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    data_naixement = DateField('Data Naixement', validators=[DataRequired()])
    sexe = StringField('Sexe', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

class QuotaAnualForm(FlaskForm):
    num_soci = StringField('Num Soci', validators=[DataRequired()])
    data_pagament = DateField('Data Pagament', validators=[DataRequired()])
    import_ = DecimalField('Import', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Afegeix altres formularis segons sigui necessari
