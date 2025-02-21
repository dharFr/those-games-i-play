import os
import requests
from typing import Dict, List, Optional
from pydantic import BaseModel

class SteamGame(BaseModel):
    app_id: int
    name: str
    price: float
    release_date: str
    tags: List[str]
    genres: List[str]
    reviews_score: Optional[float]
    total_reviews: Optional[int]

class SteamClient:
    def __init__(self):
        self.api_key = os.environ["STEAM_API_KEY"]
        self.base_url = "https://api.steampowered.com"

    def get_indie_games(self, limit: int = 100) -> List[SteamGame]:
        # Steam API endpoint for getting app list
        url = f"{self.base_url}/ISteamApps/GetAppList/v2/"
        
        response = requests.get(url)
        response.raise_for_status()
        
        apps = response.json()["applist"]["apps"]
        indie_games = []
        
        for app in apps[:limit]:  # Limit for development
            details = self._get_game_details(app["appid"])
            if details and self._is_indie_game(details):
                indie_games.append(details)
        
        return indie_games

    def _get_game_details(self, app_id: int) -> Optional[SteamGame]:
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
        response = requests.get(url)
        
        if not response.ok:
            return None
            
        data = response.json()
        if not data[str(app_id)]["success"]:
            return None
            
        game_data = data[str(app_id)]["data"]
        
        return SteamGame(
            app_id=app_id,
            name=game_data["name"],
            price=game_data.get("price_overview", {}).get("final", 0) / 100,
            release_date=game_data["release_date"]["date"],
            tags=[tag["description"] for tag in game_data.get("categories", [])],
            genres=[genre["description"] for genre in game_data.get("genres", [])],
            reviews_score=None,  # We'll add this in a separate API call
            total_reviews=None
        )

    def _is_indie_game(self, game: SteamGame) -> bool:
        return "Indie" in game.tags or "Indie" in game.genres
