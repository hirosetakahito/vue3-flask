import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config.configObject")
    db.init_app(app)
    migrate = Migrate(app, db)
    ma.init_app(app)
    from datamanage import views
    app.register_blueprint(views.bp)

    return app


app = create_app()
