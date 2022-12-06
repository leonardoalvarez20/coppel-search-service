"""
Search endpoint
"""
from fastapi import APIRouter, Depends

from app import schemas
from app.services.search_service import SearchService

router = APIRouter()


@router.get("/searchComics")
def search_characters_by_query(
    query_params: schemas.SearchQueryParams = Depends(),
    search_service: SearchService = Depends(),
):
    """
    Search characters.
    """
    return search_service.search(params=query_params)
