
class Config(object):
    SECRET_KEY = 'secret'
    DEBUG = True

class Development(Config):
    pass

class Production(Config):
    DEBUG = False
