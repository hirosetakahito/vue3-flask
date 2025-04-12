import os

class DefaultConfig:
    SECRET_KEY = os.urandom(24)
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@db/sampledb?charset=utf8'

class DevelopConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///sampledb.sqlite"

class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


if os.environ.get('FLASK_ENV') == 'production':
    configObject = ProdConfig
elif os.environ.get('FLASK_ENV') == 'test':
    configObject = TestConfig
else:
    configObject = DevelopConfig
