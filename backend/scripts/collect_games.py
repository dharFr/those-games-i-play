#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app.steam.client import SteamClient
from rich.console import Console
from rich.progress import track
import json

console = Console()

def main():
    client = SteamClient()
    
    with console.status("[bold green]Fetching indie games from Steam..."):
        games = client.get_indie_games(limit=100)  # Start with 100 for testing
    
    # Save to JSON file for now (we'll use MongoDB later)
    output_file = Path(__file__).parent.parent / "data" / "indie_games.json"
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, "w") as f:
        json.dump([game.model_dump() for game in games], f, indent=2)
    
    console.print(f"[bold green]✓[/] Saved {len(games)} indie games to {output_file}")

if __name__ == "__main__":
    main()
