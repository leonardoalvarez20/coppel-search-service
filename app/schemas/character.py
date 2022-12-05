"""
Character schema
"""
from pydantic import BaseModel


class Character(BaseModel):
    """
    Character attributes
    """

    id: int
    name: str
    image: str
    appearances: int
