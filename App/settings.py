import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 支付宝
ALIPAY_PUBLIC_KEY = open(os.path.join(BASE_DIR, "alipay/app_public_key.pem")).read()
APP_PRIVATE_KEY = open(os.path.join(BASE_DIR, "alipay/app_private_key.pem")).read()
ALIPAY_APPID = "2016101200666318"

def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE') or 'sqlite'
    driver = dbinfo.get('DRIVER') or 'sqlite'
    user = dbinfo.get('USER') or ''
    password = dbinfo.get('PASSWORD') or ''
    host = dbinfo.get('HOST') or ''
    port = dbinfo.get('PORT') or ''
    name = dbinfo.get('NAME') or ''

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        'USER': 'root',
        'PASSWORD': '818919',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'taopp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        'USER': 'root',
        'PASSWORD': '818919',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'taopp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        'USER': 'root',
        'PASSWORD': '818919',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'taopp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        'USER': 'root',
        'PASSWORD': '818919',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'taopp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}

ADMINS = ('duan', 'run')
FILE_PATH_PREFIX = '/static/uploads/icons'
UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')
