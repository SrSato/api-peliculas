# configuración por defecto
SECRET_KEY = 'MiClaveSuperSecretaInvencibleChachiGuachi'
JWT_SECRET_KEY = SECRET_KEY = 'MiClaveSuperSecretaInvencibleChachiGuachi'

PROPAGATE_EXCEPTIONS = True # Con True manejamos las excep a nivel de aplicacion (nosotros mismos)

# DB Config
SQLALCHEMY_DATABASE_URI = 'sqlite:///films.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False # Docu de SQLALCHEMY: para prod desactivada esta opcion
SHOW_SQLALCHEMY_LOG_MESSAGES = False # Esto es para no tener que gestionar los logs ;)

ERROR_404_HELP = False # Si lo pones a True da pistas sobre posibles endpoints parecidos al que no hay
