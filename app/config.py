import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = """os.environ.get('SECRET_KEY') or """ 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = """ os.environ.get('DATABASE_URL') or """ 'postgresql://yourusername:yourpassword@localhost/databasename'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    ADMIN_USERNAME = """os.environ.get('ADMIN_USERNAME') or """ 'czyjuokoevhdhq'
    ADMIN_PASSWORD = """os.environ.get('ADMIN_PASSWORD') or """ '2feee4448201b61e6725928d401d5cf91ed4a8b7e94b729478dd21b177257aa4'
    UPLOAD_FOLDER = './uploads'
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False