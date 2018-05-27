import os


class Config:

    SECRET_KEY = 'AbeautifulSecretKey'
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:psql@localhost/pitchit')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:Dedecocomagna1@localhost/pitchit')
    pass

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}