#!/usr/bin/python3
''' A class that defines all common attributes/methods for other classes '''

from datetime import datetime
from uuid import uuid4


class BaseModel:
    ''' Base/parent class '''
    def __init__(self):
        ''' constructor to initialize class '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        d = self.__dict__.copy()
        return "[{}] ({}) <{}>".format(type(self).__name__, self.id, d)

    def save(self):
        ''' updates the updated_at with the current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' dictionary containing all keys/values of __dict__ of instance '''

        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
