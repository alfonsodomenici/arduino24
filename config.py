class Config:
    JWT_SECRET_KEY='my secret key'
    TESTING=False
    JSONIFY_PRETTYPRINT_REGULAR=True
    
class TestConfig(Config):
    TESTING=True

class DevConfig(Config):
    MYSQL_USER="root"
    MYSQL_PASSWORD="root"
    MYSQL_DB="arduino24"
    MYSQL_CURSORCLASS="DictCursor"

class ProdConfig(Config):
    MYSQL_USER="root"
    MYSQL_PASSWORD="root"
    MYSQL_DB="arduino24"
    MYSQL_CURSORCLASS="DictCursor"

configDict={
    'development':DevConfig,
    'testing':TestConfig,
    'production':ProdConfig,
    'default':DevConfig
}