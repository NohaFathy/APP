#!usr/bin/pyhton3
"""define the user class"""

from models.basemodel import BaseModel
class User(BaseModel):
    """attributes:"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
