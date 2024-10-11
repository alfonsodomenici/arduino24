from flask import Flask
from config import configDict
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = MySQL()
jwt=JWTManager()
cors = CORS()

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName])
    
    db.init_app(app)
    jwt.init_app(app)
    
    from .api import api 
    app.register_blueprint(api)

    cors.init_app(app ,resources={r"/api/*": {"origins":"*"}})
    return app