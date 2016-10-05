
class Config(object):
    SECRET_KEY = 'secret'
    DEBUG = True
    CACHE_TIMEOUT = 3600 #Default cache timeout is 1 hour

class Development(Config):
    pass

class Production(Config):
    DEBUG = False
