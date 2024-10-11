from flask import Blueprint

api = Blueprint('api',__name__,url_prefix='/api')

from .arduinosResource import arduinos
api.register_blueprint(arduinos)

from .authResource import auths
api.register_blueprint(auths)