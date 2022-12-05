"""
Comic Schema
"""
from datetime import datetime

from pydantic import BaseModel


class Comic(BaseModel):
    """
    Comic Attributes
    """

    id: int
    title: str
    image: str
    on_sale_date: datetime
