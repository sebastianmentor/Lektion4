from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Bok(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(80), nullable=False)
    forfattare = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    pris = db.Column(db.Float, nullable=False)
    lagerantal = db.Column(db.Integer, nullable=False)
    bestallningsdetaljer = db.relationship('BestallningsDetalj', backref='bok', lazy=True)

class Kund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100), nullable=False)
    epost = db.Column(db.String(120), unique=True, nullable=False)
    telefonnummer = db.Column(db.String(20), nullable=False)
    adress = db.Column(db.String(200), nullable=False)
    bestallningar = db.relationship('Bestallning', backref='kund', lazy=True)

class Bestallning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kund_id = db.Column(db.Integer, db.ForeignKey('kund.id'), nullable=False)
    bestallningsdatum = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    leveransstatus = db.Column(db.String(20), nullable=False)
    detaljer = db.relationship('BestallningsDetalj', backref='bestallning', lazy=True)

class BestallningsDetalj(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bestallning_id = db.Column(db.Integer, db.ForeignKey('bestallning.id'), nullable=False)
    bok_id = db.Column(db.Integer, db.ForeignKey('bok.id'), nullable=False)
    antal = db.Column(db.Integer, nullable=False)
    pris_per_enhet = db.Column(db.Float, nullable=False)

class Tidningar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(80), nullable=False)
    forfattare = db.Column(db.String(50), nullable=False)
    pris = db.Column(db.Float, nullable=False)
    lagerantal = db.Column(db.Integer, nullable=False)

# Lägg till andra tabeller som Anställda här om det behövs
