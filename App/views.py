from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Membre, Equip, Competicio, Entrenament, Patrocinador, PaquetDePatrocini

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    membres = Membre.query.all()
    return render_template('member.html', membres=membres)

@app.route('/teams')
def teams():
    equips = Equip.query.all()
    return render_template('team.html', equips=equips)

@app.route('/competitions')
def competitions():
    competicions = Competicio.query.all()
    return render_template('competition.html', competicions=competicions)

@app.route('/trainings')
def trainings():
    entrenaments = Entrenament.query.all()
    return render_template('training.html', entrenaments=entrenaments)

@app.route('/sponsors')
def sponsors():
    patrocinadors = Patrocinador.query.all()
    return render_template('sponsor.html', patrocinadors=patrocinadors)

@app.route('/packages')
def packages():
    paquets = PaquetDePatrocini.query.all()
    return render_template('package.html', paquets=paquets)
