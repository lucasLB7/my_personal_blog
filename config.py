import os


class Config:

    SECRET_KEY = 'AbeautifulSecretKey'
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:psql@localhost/blog')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True


    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "blenderfendermail@gmail.com"

    MAIL_PASSWORD = "BlenderFender1"



class TestConfig(Config):
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:psql@localhost/blog')
    

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}