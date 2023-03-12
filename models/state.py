#!/usr/bin/python3
"""Define state model"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents State model

    Args:
        name (str): name of state
    """
    name = ""
