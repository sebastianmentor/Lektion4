from flask import Flask, render_template
from flask_migrate import Migrate, upgrade
from models import db, seed_data, Bok

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


if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data()

    app.run(debug=True)