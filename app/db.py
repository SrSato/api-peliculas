# configuracion de la base de datos
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
Clase para los métodos comunes de todos los modelos que vayamos a usar.

'''
class BaseModelMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()