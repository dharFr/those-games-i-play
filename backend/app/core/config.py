from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # API Settings
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    project_name: str = "Those Games I Play"
    version: str = "0.1.0"
    
    # CORS
    allowed_origins: List[str] = ["http://localhost:5173"]
    
    # Database
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "those_games_i_play"
    
    # Redis
    redis_url: str = "redis://localhost:6379"
    redis_ttl: int = 3600  # 1 hour default cache TTL
    
    # Steam
    steam_api_key: str  # No default value = required field
    steam_api_url: str = "https://api.steampowered.com"
    
    # Pagination
    default_page_size: int = 20
    max_page_size: int = 100

    class Config:
        # This tells pydantic to load .env file
        # The loading order is:
        # 1. Environment variables (export STEAM_API_KEY=xxx)
        # 2. .env file variables (make sure to add .env to .gitignore)
        # 3. Default values defined above
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
