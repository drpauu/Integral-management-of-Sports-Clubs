from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Membre(db.Model):
    __tablename__ = 'membre'
    num_soci = db.Column(db.String, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    data_naixement = db.Column(db.Date, nullable=False)
    sexe = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

class Quota_Anual(db.Model):
    __tablename__ = 'quota_anual'
    num_soci = db.Column(db.String, db.ForeignKey('membre.num_soci'), primary_key=True)
    data_pagament = db.Column(db.Date, primary_key=True)
    import_ = db.Column(db.Numeric, nullable=False)

# Afegeix altres models segons sigui necessari
