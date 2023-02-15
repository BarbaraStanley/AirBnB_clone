#!/usr/bin/python3
"""Module that serializes instances to a JSON file and
deserializes JSON file to instances"""

import datetime
import json
import os
from models.base_model import BaseModel

class FileStorage:

    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        print(key)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)"""
        object_dict = {}
        print(FileStorage.__objects)
        for key, value in FileStorage.__objects.items():
            object_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w") as json_file:
            json_file.write(json.dumps(object_dict))

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        # from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict_json = json.load(f)
                for key, value in obj_dict_json.items():
                    class_name = value['__class__']
                    # obj = eval(class_name)(**value)
                    self.new(eval(class_name)(**value))
                """
                for o in json.load(f).values():
                    name = o["__class__"]
                    # del o["__class__"]
                    print("Here")
                    newobj = eval(name)(**o)
                    self.new(newobj)
                """
        except FileNotFoundError:
            return
