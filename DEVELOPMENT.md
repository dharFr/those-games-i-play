# Development Setup

## Prerequisites

1. Install mise:
   ```bash
   curl https://mise.jdx.dev/install.sh | sh
   ```

2. Install 1Password CLI and login:
   ```bash
   op signin
   ```

## Quick Start

1. Install all tools and dependencies:
   ```bash
   mise install
   mise run install
   ```

2. Start all services:
   ```bash
   mise run start
   ```

3. Stop all services:
   ```bash
   mise run stop
   ```

## Service URLs

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Data Import Workflow

1. Collect game data from Steam:
   ```bash
   mise run collect-games
   ```
   This will fetch indie games from Steam API and save them to `backend/data/indie_games.json`

2. Import games into MongoDB:
   ```bash
   mise run import-games
   ```
   This will process the JSON file and import games into the MongoDB database.

## Development Tools

### Recommended VSCode Extensions
- Python
- Pylance
- Vue Language Features
- TypeScript Vue Plugin
- ESLint
- Prettier

### Code Style
- Backend: Black formatter
- Frontend: Prettier + ESLint
