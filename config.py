import os 

class Config: 
    DEBUG = False
    TESTING = False   
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY='secret_key_just_for_dev_environment'
    SQLALCHEMY_DATABASE_URI='sqlite:///devDB.sqlite'

class TestConfig(Config): 
    TESTING = True
    SECRET_KEY='secret_key_just_for_test_environment'
    SQLALCHEMY_DATABASE_URI='sqlite:///testDB.sqlite'