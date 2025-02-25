#!/usr/bin/env python3
import sys
from pathlib import Path
import json
from datetime import datetime
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from rich.console import Console
from rich.progress import track
import locale

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))
from app.core.config import settings

console = Console()

def parse_date(date_str: str) -> datetime:
    """Parse date string in various formats."""
    date_formats = [
        '%d %b',           # "22 Oct"
        '%d/%b./%Y',       # "9/ago./2018"
        '%d/%m/%Y',        # "09/08/2018"
        '%Y-%m-%d',        # "2018-08-09"
        '%d %b, %Y',       # "22 Oct, 2018"
    ]
    
    # Clean up the date string
    date_str = date_str.split(',')[0]  # Remove year if separated by comma
    
    # Try each format
    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            continue
    
    # If all formats fail, log the error and return a default date
    console.print(f"[yellow]Warning: Could not parse date '{date_str}'. Using default date.[/yellow]")
    return datetime(2000, 1, 1)  # Default to January 1, 2000

def transform_game(game_data: dict) -> dict:
    """Transform raw JSON game data to match our Game model structure."""
    try:
        # Parse the release date
        release_date = parse_date(game_data['release_date'])
        
        # Convert price to float, handle potential string values
        price_str = str(game_data["price"]).replace(',', '.')
        try:
            price = float(price_str)
        except ValueError:
            price = 0.0
            console.print(f"[yellow]Warning: Invalid price for {game_data['name']}, using 0.0[/yellow]")
        
        return {
            "steam_id": game_data["app_id"],
            "title": game_data["name"],
            "genres": game_data["genres"],
            "tags": game_data["tags"],
            "price": price,
            "release_date": release_date,
            "review_score": game_data["reviews_score"],
            "review_count": game_data["total_reviews"]
        }
    except Exception as e:
        console.print(f"[red]Error transforming game {game_data.get('name', 'Unknown')}: {str(e)}[/red]")
        return None

async def import_games():
    # Connect to MongoDB
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.database_name]
    collection = db.games
    
    try:
        # Read JSON file
        json_path = Path(__file__).parent.parent / "data" / "indie_games.json"
        with open(json_path, 'r') as f:
            games_data = json.load(f)
        
        # Transform and import games
        console.print(f"[bold blue]Found {len(games_data)} games to import[/bold blue]")
        
        # Create index on steam_id to ensure uniqueness
        await collection.create_index("steam_id", unique=True)
        
        success_count = 0
        error_count = 0
        
        for game_data in track(games_data, description="Importing games..."):
            transformed_game = transform_game(game_data)
            if transformed_game:
                try:
                    # Use upsert to update if exists or insert if new
                    await collection.update_one(
                        {"steam_id": transformed_game["steam_id"]},
                        {"$set": transformed_game},
                        upsert=True
                    )
                    success_count += 1
                except Exception as e:
                    console.print(f"[red]Error importing {transformed_game['title']}: {str(e)}[/red]")
                    error_count += 1
            else:
                error_count += 1
        
        console.print(f"[bold green]✓ Import complete![/bold green]")
        console.print(f"Successfully imported: {success_count}")
        console.print(f"Errors: {error_count}")
    
    finally:
        # Ensure client is properly closed
        if client:
            client.close()

if __name__ == "__main__":
    asyncio.run(import_games())
