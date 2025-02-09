from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # These are default values that will be overridden by environment variables
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "those_games_i_play"
    redis_url: str = "redis://localhost:6379"
    # No default value means this setting is required
    steam_api_key: str

    class Config:
        # This tells pydantic to load .env file
        # The loading order is:
        # 1. Environment variables (export STEAM_API_KEY=xxx)
        # 2. .env file variables (make sure to add .env to .gitignore)
        # 3. Default values defined above
        env_file = ".env"

settings = Settings()
