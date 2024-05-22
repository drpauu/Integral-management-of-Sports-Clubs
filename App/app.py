from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Membre, Quota_Anual
from forms import MembreForm, QuotaAnualForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# Rutes per Membres
@app.route('/membres')
def membres():
    membres = Membre.query.all()
    return render_template('membre/membre_list.html', membres=membres)

@app.route('/membre/<num_soci>')
def membre_detail(num_soci):
    membre = Membre.query.get(num_soci)
    return render_template('membre/membre_detail.html', membre=membre)

@app.route('/membre/add', methods=['GET', 'POST'])
def add_membre():
    form = MembreForm()
    if form.validate_on_submit():
        new_membre = Membre(
            num_soci=form.num_soci.data,
            nom=form.nom.data,
            data_naixement=form.data_naixement.data,
            sexe=form.sexe.data,
            email=form.email.data
        )
        db.session.add(new_membre)
        db.session.commit()
        return redirect(url_for('membres'))
    return render_template('membre/membre_add.html', form=form)

@app.route('/membre/edit/<num_soci>', methods=['GET', 'POST'])
def edit_membre(num_soci):
    membre = Membre.query.get(num_soci)
    form = MembreForm(obj=membre)
    if form.validate_on_submit():
        membre.nom = form.nom.data
        membre.data_naixement = form.data_naixement.data
        membre.sexe = form.sexe.data
        membre.email = form.email.data
        db.session.commit()
        return redirect(url_for('membre_detail', num_soci=num_soci))
    return render_template('membre/membre_edit.html', form=form)

@app.route('/membre/delete/<num_soci>', methods=['POST'])
def delete_membre(num_soci):
    membre = Membre.query.get(num_soci)
    db.session.delete(membre)
    db.session.commit()
    return redirect(url_for('membres'))

# Rutes per Quota Anual
@app.route('/quotas')
def quotas():
    quotas = Quota_Anual.query.all()
    return render_template('quota_anual/quota_list.html', quotas=quotas)

@app.route('/quota/add', methods=['GET', 'POST'])
def add_quota():
    form = QuotaAnualForm()
    if form.validate_on_submit():
        new_quota = Quota_Anual(
            num_soci=form.num_soci.data,
            data_pagament=form.data_pagament.data,
            import_=form.import_.data
        )
        db.session.add(new_quota)
        db.session.commit()
        return redirect(url_for('quotas'))
    return render_template('quota_anual/quota_add.html', form=form)

# Afegeix rutes per altres entitats segons sigui necessari

if __name__ == '__main__':
    app.run(debug=True)
