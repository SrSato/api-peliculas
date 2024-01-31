# El RegEdit de la aplicacion
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

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
    jwt = JWTManager(app)


    Api(app,catch_all_404s=True)

    app.url_map.strict_slashes = False

    app.register_blueprint(films_v1_0_bp)
    
    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg':'Internal server error'}), 500
    
    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg':'Method not allowed'}), 405
    
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg':'Not Found error'}), 404
    
    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg':'Forbidden error'}), 403
    
    @app.errorhandler(401)
    def handle_401_error(e):
        return jsonify({'msg': 'Bad username or password'}),401
    
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg':'str(e)'}), 500
    
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg':str(e)}), 404