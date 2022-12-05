"""
Application API routes
"""

from fastapi import APIRouter, status

from app.api.api_V1.endpoints import search

api_router = APIRouter()

"""
Search Endpoints
"""
api_router.include_router(
    search.router,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
