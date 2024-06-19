from app import db

class Membre(db.Model):
    __tablename__ = 'membre'
    num_soci = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    data_naixement = db.Column(db.Date, nullable=False)
    sexe = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

class Equip(db.Model):
    __tablename__ = 'equip'
    nom = db.Column(db.String, primary_key=True)
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    esport = db.Column(db.String, nullable=False)

class Competicio(db.Model):
    __tablename__ = 'competicio'
    nom = db.Column(db.String, primary_key=True)
    esport = db.Column(db.String, nullable=False)
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    any_celebracio = db.Column(db.Integer, nullable=False)

class Entrenament(db.Model):
    __tablename__ = 'entrenament'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    lloc = db.Column(db.String, nullable=False)
    esport = db.Column(db.String, nullable=False)
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)

class Patrocinador(db.Model):
    __tablename__ = 'patrocinador'
    nom = db.Column(db.String, primary_key=True)
    descripcio_beneficis = db.Column(db.String, nullable=False)

class PaquetDePatrocini(db.Model):
    __tablename__ = 'paquet_de_patrocini'
    id = db.Column(db.Integer, primary_key=True)
    beneficis = db.Column(db.String, nullable=False)
