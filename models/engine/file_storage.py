#!/usr/bin/python3
"""
Module for file storage
"""
import json
from os.path import exists


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

        with open(self.__file_path, "w", encoding="UTF-8") as text_file:
            obj_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
            json.dump(obj_dict, text_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if JSON file exists
        Otherwise do nothing. If the file doesn't exist no exception should
        be raised
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as text_file:
                self.__objects = json.load(text_file)
        except FileNotFoundError:
            pass
