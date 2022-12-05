"""
Base Marvel Params
"""
import hashlib
from functools import lru_cache

from app.config.marvel import get_marvel_settings

ts = "1"


@lru_cache
def get_base_params():
    """
    Return base Marvel dict
    """
    marvel_settings = get_marvel_settings()
    hash = hashlib.md5(
        (
            ts
            + marvel_settings.marvel_private_key
            + marvel_settings.marvel_public_key
        ).encode()
    ).hexdigest()
    return {"apikey": marvel_settings.marvel_public_key, "ts": ts, "hash": hash}
