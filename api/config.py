import os
import yaml

basedir = os.path.abspath(os.path.dirname(__file__))
db_config = yaml.safe_load(open(os.path.join(basedir,'db.yaml')))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        db_config['db']['type'],
        db_config['db']['user'],
        db_config['db']['password'],
        db_config['db']['host'],
        db_config['db']['port'],
        db_config['db']['database']
        )

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
