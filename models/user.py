#!/usr/bin/python3

"""
Holds class User
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """
    Representation of a user
    """

    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing the user
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
        Setting a password encrypted by md5
        """

        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)