import os

# BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_uri(dbinfo):
    engine = dbinfo.get('engine')
    driver = dbinfo.get('driver')
    user = dbinfo.get('user')
    password = dbinfo.get('password')
    host = dbinfo.get('host')
    port = dbinfo.get('port')
    database_name = dbinfo.get('database_name')

    # uri配置格式      使用的数据库名+驱动://用户名:密码@主机:端口/具体哪一个数据库
    return f'{engine}+{driver}://{user}:{password}@{host}:{port}/{database_name}'


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    ENV = 'develop'
    DEBUG = True

    dbinfo = {
        'engine': 'mysql',
        'driver': 'pymysql',
        'user': 'pengfan758258',
        'password': 'Pf@7758258',
        'host': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'port': '3306',
        'database_name': 'myapp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True

    dbinfo = {
        'engine': 'mysql',
        'driver': 'pymysql',
        'user': 'pengfan758258',
        'password': 'Pf@7758258',
        'host': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'port': '3306',
        'database_name': 'myapp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


class StagingConfig(Config):
    ENV = "staging"

    dbinfo = {
        'engine': 'mysql',
        'driver': 'pymysql',
        'user': 'pengfan758258',
        'password': 'Pf@7758258',
        'host': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'port': '3306',
        'database_name': 'myapp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


class ProductConfig(Config):
    ENV = 'product'

    dbinfo = {
        'engine': 'mysql',
        'driver': 'pymysql',
        'user': 'pengfan758258',
        'password': 'Pf@7758258',
        'host': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'port': '3306',
        'database_name': 'myapp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}
