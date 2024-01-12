#!/usr/bin/python3
"""
- User class model which inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a user created with the BaseModel.
    It would have the following attributes
        - email: (str)
        - password: (str)
        - first_name: (str)
        - last_name: (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
