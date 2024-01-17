from flask import Flask, render_template, request
from flask_migrate import Migrate, upgrade
from models import db, seed_data, Bok, Kund, Bestallning, BestallningsDetalj

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/LLB'


db.app = app
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template("index.html", active_page = 'start_page')

@app.route('/bocker')
def bocker():
    sort_column = request.args.get('sort_column', 'titel')
    sort_order = request.args.get('sort_order', 'asc')

    all_books = Bok.query.all()

    return render_template(
        "bocker.html", 
        all_books=all_books, 
        active_page = 'bocker_page', 
        sort_column=sort_column,
        sort_order=sort_order)

@app.route('/bocker/bok/<bokid>')
def bok(bokid):
    # b = Bok.query.filter_by(id=bokid).first()
    # b = Bok.query.where(Bok.id == bokid).first()
    b = Bok.query.filter(Bok.id == bokid).first()
    return render_template("bok.html", bok=b, active_page = 'bocker_page')

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html", active_page = 'kontakt_page')

@app.route('/kunder')
def kunder():
    alla_kunder = Kund.query.all()
    return render_template("kunder.html", kunder=alla_kunder, active_page = 'kund_page')


@app.route('/kund/<kundid>')
def kund(kundid):
    våran_kund = Kund.query.filter_by(id=kundid).first()
    # kundens_beställningar = Bestallning.query.filter_by(kund_id=kundid).all()
    
    return render_template("kund.html", kund=våran_kund, active_page = 'kund_page')

@app.route('/orders/<bestallningid>')
def orders(bestallningid):
    bestallt = Bestallning.query.filter_by(id=bestallningid).first()

    return render_template("bestallningsdetaljer.html", bestallning=bestallt, active_page = 'kund_page' )


if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data()

    app.run(debug=True)