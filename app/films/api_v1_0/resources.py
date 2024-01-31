# Endpoints del api
from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required

from .schemas import FilmSchema, UserSchema
from ..models import Film, Actor, User
from ...common.error_handling import ObjectNotFound

films_v1_0_bp = Blueprint('films_v1_0_bp', __name__)

film_schema = FilmSchema()
user_schema = UserSchema()

api = Api(films_v1_0_bp)

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        user = User(name = user_dict['name'],
                    pwd = user_dict['pwd'])
        user.save()
        resp = user_schema.dump(user)
        return resp, 201

class TokenResource(Resource):
    def post(self):        
        name = request.json.get("name", None)
        pwd = request.json.get("pwd", None)

        user = User.query.filter_by(name=name, pwd=pwd).first()
        
        if user is None:
            raise NameError(401)
        
        access_token = create_access_token(identity = user.id)        
        resp = jsonify({"token": access_token, "user_id":user.id})
        return resp
    

class FilmListResource(Resource):
    @jwt_required()
    def get(self):
        films = Film.get_all()
        result = film_schema.dump(films, many = True)
        return result
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        film_dict = film_schema.load(data)
        film = Film(title = film_dict['title'],
                    length = film_dict['length'],
                    year = film_dict['year'],
                    director = film_dict['director'])        
        for actor in film_dict['actors']:
            film.actors.append(Actor(actor['name']))
        film.save()
        resp = film_schema.dump(film)
        return resp, 201
    
class FilmResource(Resource):
    @jwt_required()
    def get(self, film_id):        
        film = Film.get_by_id(film_id)
        if film is None:
            raise ObjectNotFound('La película no existe')
        resp = film_schema.dump(film)
        return resp
       

api.add_resource(UserResource, '/api/v1.0/users', endpoint = 'user_resource')
api.add_resource(TokenResource, '/api/v1.0/tokens', endpoint = 'token_resource')
api.add_resource(FilmListResource, '/api/v1.0/films', endpoint = 'film_list_resource')
api.add_resource(FilmResource, '/api/v1.0/films/<int:film_id>',endpoint = 'film_resource')
