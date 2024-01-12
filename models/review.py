#!/usr/bin/python3
"""
Module for the reviews class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class to handle reviews of customers
    - Attributes
        - place_id: (str) -> Place.id
        - user_id: (str) -> User.id
        - text: (str)
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
