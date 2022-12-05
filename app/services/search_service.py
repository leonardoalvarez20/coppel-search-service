"""
Handles search operation
"""
from fastapi.encoders import jsonable_encoder

from app.helpers.base_marvel_params import get_base_params
from app.schemas import Character, Comic, SearchQueryParams
from app.services.api_client import APIRequest


class SearchService:
    def __init__(self):
        self.marvel_client = APIRequest(
            base_url="https://gateway.marvel.com:443/v1/public/",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        self.marvel_params = get_base_params()

    def search(self, params: SearchQueryParams):
        """
        Execute algorithm given a value on params
        """
        if params.keyword:
            return self.search_by_keyword(params.keyword)
        elif params.character:
            return self.search_by_character(params.character)
        elif params.comic:
            return self.search_by_comic(params.comic)
        else:
            return self.search_by_character()

    def search_by_character(self, character: str = ""):
        """
        Does a search by character name, if character param is empty then get all characters
        """
        params = dict(self.marvel_params)
        if character:
            params.update({"name": character})

        result = self.marvel_client.send_request(
            method="GET", route="characters", params=params
        )
        result.raise_for_status()

        characters = []
        data = result.json()
        if data["data"]["results"]:
            for character_result in data["data"]["results"]:
                characters.append(
                    Character(
                        id=character_result["id"],
                        name=character_result["name"],
                        image=f"{character_result['thumbnail']['path']}.{character_result['thumbnail']['extension']}",
                        appearances=(
                            character_result["comics"]["available"]
                            + character_result["series"]["available"]
                            + character_result["stories"]["available"]
                        ),
                    )
                )
        return jsonable_encoder(characters)

    def search_by_comic(self, comic: str = ""):
        """
        Does search by comic, if comic param is empty then get all comics
        """
        params = dict(self.marvel_params)
        if comic:
            params.update({"title": comic})

        result = self.marvel_client.send_request(
            method="GET", route="comics", params=params
        )
        result.raise_for_status()

        comics = []
        data = result.json()
        if data["data"]["results"]:
            for comic_result in data["data"]["results"]:
                comics.append(
                    Comic(
                        id=comic_result["id"],
                        title=comic_result["title"],
                        image=f"{comic_result['thumbnail']['path']}.{comic_result['thumbnail']['extension']}",
                        on_sale_date=comic_result["dates"][0]["date"],
                    )
                )
        return jsonable_encoder(comics)

    def search_by_keyword(self, keyword: str):
        """
        Search on characters and comics given a keyword
        """
        result_characters = self.search_by_character(character=keyword)
        result_comics = self.search_by_comic(comic=keyword)

        return {"characters": result_characters, "comics": result_comics}
