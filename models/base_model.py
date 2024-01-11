#!/usr/bin/python3
"""
Module for the Base Class
- Public instance attributes
    - id
    - created_at
    - updated_at
- Public instance methods
    - save(self) - updates the updated_at attribute
    - to_dict(self) - returns dictionary
- __str__ method to print
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This is the base model class
    It is an abstract class from which all other classes would inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initialiazes new instance of BaseModel.

        Args:
            *args: Unused positional arguments
            **kwargs: Dictionary representation of an instance.

        If kwargs is not empty:
            Each key has an attribute name
            Each value is the value of the corresponding attr name
            Convert datetime to datetime objects

        Otherwise:
            Create id and created_at values as initially done
        """
        if kwargs:
            if '__class__' in kwargs:
                # Remove '__class__' from the dictionary
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the object class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute update_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing key/value of __dict__ for an instance
        """

        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
