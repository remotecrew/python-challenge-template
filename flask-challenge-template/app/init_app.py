from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
csrf = CSRFProtect()
ma = Marshmallow()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'b3be5f02a4ca515eadd92d7fd8da1382f5934131a153403d86b0a34cdd4c1861'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volleyball.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.config['WTF_CSRF_ENABLED'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app) 
    ma.init_app(app)

    return app
