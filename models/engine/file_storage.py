#!/usr/bin/python3
"""
Module for file storage
"""
import json
# from os.path import exists


class FileStorage:
    """
    - Serializes instances to JSON
    - Deserializes JSON to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """
        Sets an object in __objects with key <obj_class>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects into JSON file (path __file_path)
        """
        obj_dict = {}
        for key, obj in self.all().items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as text_file:
            json.dump(obj_dict, text_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if JSON file exists
        Otherwise do nothing. If the file doesn't exist no exception should
        be raised
        """
        from models.base_model import BaseModel

        class_map = {
                    'BaseModel': BaseModel,
            }

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as text_file:
                obj_dict = json.load(text_file)

                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    class_instance = class_map[class_name]
                    instance = class_instance(**val)
                    all_objects = self.all()
                    all_objects[key] = instance
        except FileNotFoundError:
            pass
