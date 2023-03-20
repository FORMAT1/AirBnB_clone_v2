#!/usr/bin/python3
""" New engine DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, session, scoped_session, relationship
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage():
    """ DBStorage Class """
    __engine = None
    __session = None

    def __init__(self):
        """ init method """
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        mysql_env = getenv('HBNB_ENV') 

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_pwd, mysql_host, mysql_db), pool_pre_ping=True)

        if mysql_env == 'test'
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all method """
        if cls:
            objs = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for _class in classes:
                objs += self.__session.query(_class)
        """to create and save data"""
        new_dict = {}
    
        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ new method """
        self.__session.add(obj)

    def save(self):
        """ save method to commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete method to delete from the 
            current database
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """to create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        """to create current session in the db"""
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ close method """
        if self.__session:
            self.__session.close()
