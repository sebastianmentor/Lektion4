from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from faker import Faker
import random

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


def seed_data():
    fake = Faker()

    nr_of_books = Bok.query.count()
    if nr_of_books < 500:
        for _ in range(100):
            title = fake.catch_phrase()
            author = fake.name()
            isbn = fake.isbn13()
            price = random.randint(50, 400)
            inventory = random.randint(0, 10000)

            bok = Bok(titel=title,
                    forfattare=author,
                    isbn=isbn,
                    pris=price,
                    lagerantal=inventory)
            db.session.add(bok)
            db.session.commit()


    nr_of_customers = Kund.query.count()
    if nr_of_customers < 1000:
        fake2 = Faker('sv_SE')  # Svensk lokaliseringsinställning
        kunder = []
        while nr_of_customers <= 1000:
            kund = {
                "namn": fake2.name(),
                "adress": fake2.address(),
                "epost": fake2.email(),
                "telefonnummer": fake2.phone_number()
            }
            kunden_finns = Kund.query.filter_by(epost=kund['epost']).first()
            print(Kund.query.filter_by(epost=kund['epost']))
            print(Kund.query.filter_by(epost='candersson@example.com'))
            print(Kund.query.filter_by(epost='candersson@example.com').first())
            if not kunden_finns:    
                kunder.append(kund)
                nr_of_customers += 1

        # Exempel på att skapa 10 fejkade kunder
        for kund in kunder:
            db.session.add(Kund(**kund))
            db.session.commit()


