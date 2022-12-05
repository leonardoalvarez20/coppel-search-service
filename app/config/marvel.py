"""
Marvel Settings
"""
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Marvel Settings

    Attributes:
        marvel_public_key:
        marvel_private_key:
        marvel_api
    """

    marvel_public_key: Optional[str]
    marvel_private_key: Optional[str]
    marvel_api: Optional[str]


settings = Settings()


@lru_cache
def get_marvel_settings():
    """
    Return Marvel Settings
    """
    return Settings()
