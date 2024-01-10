from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/LLB'


db.app = app
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return "Hej"


if __name__ == '__main__':
    with app.app_context():
        upgrade()
    
    app.run(debug=True)