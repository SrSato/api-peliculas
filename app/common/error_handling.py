# Utilidades para el manejo de errores

''' Todas las excepciones heredarán de aquí '''
class AppErrorBaseClass(Exception):
    pass

''' Para los accesos a cosas que no existen '''
class ObjectNotFound(AppErrorBaseClass):
    pass