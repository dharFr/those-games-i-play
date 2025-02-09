# Development Setup

## Prerequisites

- Python 3.11+
- Node.js 18+
- MongoDB 6.0+
- Redis 7.0+
- Steam API key ([Get it here](https://steamcommunity.com/dev/apikey))
- direnv ([Installation guide](https://direnv.net/))
- 1Password CLI ([Installation guide](https://1password.com/downloads/command-line/))

## Backend Setup

1. Configure your shell for direnv:
   ```bash
   # Add to your ~/.zshrc or ~/.bashrc
   eval "$(direnv hook zsh)"  # or bash
   ```

2. Configure 1Password CLI:
   ```bash
   # Sign in to 1Password CLI
   op signin
   ```

3. Create a Python virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure environment:
   - Copy `.env.example` to `.env` and adjust database URLs if needed
   - Create `.envrc` file (it will be auto-loaded by direnv)
   - Run `direnv allow` to approve the .envrc file

6. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at http://localhost:8000

## Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at http://localhost:5173

## Database Setup

1. Start MongoDB:
   ```bash
   mongod
   ```

2. Start Redis:
   ```bash
   redis-server
   ```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

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
