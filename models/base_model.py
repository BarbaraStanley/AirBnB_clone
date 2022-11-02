#!/usr/bin/python3
''' A class that defines all common attributes/methods for other classes '''

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    ''' Base/ parent class'''

    def __init__(self, *args, **kwargs):
        '''Class initialization'''
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        storage.new(self)
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self, remove_password=True):
        """Return a dictionary representation of the BaseModel instance.
        Includes the key/value pair __class__ representing the class name
        of the object
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        d = self.__dict__.copy()
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

