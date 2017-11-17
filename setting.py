# -*-coding=utf-8-*-
from toolkit import Toolkit
from sqlalchemy import create_engine
import redis
MYSQL_USER = Toolkit.getUserData('data.cfg')['MYSQL_USER']
MYSQL_PASSWORD = Toolkit.getUserData('data.cfg')['MYSQL_PASSWORD']
MYSQL_HOST = Toolkit.getUserData('data.cfg')['MYSQL_HOST']
MYSQL_PORT = Toolkit.getUserData('data.cfg')['MYSQL_PORT']
DB = 'history'
REDIS_HOST='localhost'
engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, DB))
