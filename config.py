import os


class Config:

    SECRET_KEY = 'AbeautifulSecretKey'
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:psql@localhost/pitchit')
=======
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:psql@localhost/blogdb')
>>>>>>> 9e8c0c8e18be9227b31f24853ec841f53d9a7723
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    pass


class ProdConfig(Config):
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:Dedecocomagna1@localhost/pitchit')
=======
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'postgresql+psycopg2://d4rkkn1t3:Dedecocomagna1@localhost/blogdb')
>>>>>>> 9e8c0c8e18be9227b31f24853ec841f53d9a7723
    pass

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
<<<<<<< HEAD
}
=======
}
>>>>>>> 9e8c0c8e18be9227b31f24853ec841f53d9a7723
