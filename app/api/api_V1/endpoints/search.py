"""
Search endpoint
"""
from fastapi import APIRouter, Depends

from app import schemas
from app.services.search_service import SearchService
from app.services.user_service import UserService

router = APIRouter()

user_service_instance = UserService()


def validate_token(is_valid=Depends(user_service_instance)):
    return is_valid


@router.get("/searchComics")
def search_characters_by_query(
    _is_token_valid: bool = Depends(validate_token),
    query_params: schemas.SearchQueryParams = Depends(),
    search_service: SearchService = Depends(),
):
    """
    Search characters.
    """
    return search_service.search(params=query_params)
