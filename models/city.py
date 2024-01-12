#!/usr/bin/python3
"""
The module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class to represent the various cities
    - Attributes
        - state_id: (str) -> State.id
        - name: (str)
    """

    state_id: str = ""
    name: str = ""
