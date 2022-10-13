import os
import yaml

basedir = os.path.abspath(os.path.dirname(__file__))
db_config = yaml.safe_load(open(os.path.join(basedir,'db.yaml')))

def get_db():
    db = db_config['db']
    uri = '{}://'.format(db['type'])
    user = db.get('user',None)
    if user:
        uri = uri + user
        pw = db.get('password',None)
        if pw:
            uri = uri + ':' + pw
        uri = uri + '@'

    host = db.get('host',None)
    if host:
        uri = uri + host
        port = db.get('port',None)
        if port:
            uri = uri + ':{}'.format( port )
    uri = uri + '/' + db.get('database') 
    return uri

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = get_db()


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
