"""
Search Query Params
"""
from typing import Optional

from pydantic import BaseModel


class SearchQueryParams(BaseModel):
    """
    Search Attributes
    """

    comic: Optional[str]
    character: Optional[str]
    keyword: Optional[str]
