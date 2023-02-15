#!/usr/bin/python3
''' A class that defines all common attributes/methods for other classes '''

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    ''' Base/parent class '''
    def __init__(self, *args, **kwargs):
        ''' constructor to initialize class'''

        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    setattr(self, k, v)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        d = self.__dict__.copy()
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def save(self):
        ''' updates the updated_at with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' dictionary containing all keys/values of __dict__ of instance '''

        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
