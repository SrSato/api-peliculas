# El RegEdit de la aplicacion
from flask import Flask, jsonify
from flask_restful import Api

from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.films.api_v1_0.resources import films_v1_0_bp
from .ext import ma, migrate

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    #Vamos con las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    Api(app,catch_all_404s=True)

    app.url_map.strict_slashes = False

    app.register_blueprint(films_v1_0_bp)
    
    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app. ###### PARAMOS AQUI: 30/01/2024