from flask import Flask, render_template
from flask_migrate import Migrate, upgrade
from models import db, seed_data, Bok, Kund, Bestallning, BestallningsDetalj

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/LLB'


db.app = app
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bocker')
def bocker():
    all_books = Bok.query.all()
    return render_template("bocker.html", all_books=all_books)

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/kunder')
def kunder():
    alla_kunder = Kund.query.all()
    return render_template("kunder.html", kunder=alla_kunder)


@app.route('/kund/<kundid>')
def kund(kundid):
    våran_kund = Kund.query.filter_by(id=kundid).first()
    kundens_beställningar = Bestallning.query.filter_by(kund_id=kundid).all()
    return render_template("kund.html", kund=våran_kund, )


if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data()

    app.run(debug=True)