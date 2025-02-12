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
