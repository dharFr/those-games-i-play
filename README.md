# Those Games I Play

An indie video game explorer app.

## MVP - Essential Features:

- List of games with basic filters (genre, year)
- Detailed view of a game
- Simple visualization of relationships between similar games
- Basic recommendation system

### Data Source for the MVP:

- Steam API only (to start)
- Focus on indie games from the last 5 years
- Main data: title, genre, tags, price, release date, reviews

## Technical Stack
- Vue.js + Pinia + TypeScript for the frontend
- D3.js for visualizations
- Python/FastAPI for the API
- Pandas/Polars for data processing
- MongoDB for storage
- Redis for caching
- Scikit-learn for predictions

## Development

For detailed instructions about setting up the development environment, see [DEVELOPMENT.md](DEVELOPMENT.md)

## Target Roadmap:

### Iteration 1 - Setup & Data (1-2 evenings)

- [ ] Project setup (front/back)
- [ ] Simple Steam API collection script
- [ ] Basic MongoDB storage
- [ ] Stack testing

### Iteration 2 - Basic Frontend (2-3 evenings)

- [ ] List of games with simple filters
- [ ] Detailed view of a game
- [ ] Basic navigation
- [ ] Minimal but clean style

### Iteration 3 - First Visualization (2-3 evenings)

- [ ] Simple graph of similar games with D3.js
- [ ] Basic interactions (zoom, click)
- [ ] Filters on the graph

### Iteration 4 - Recommendations (2-3 evenings)

- [ ] Simple algorithm based on tags/genres
- [ ] Display of recommendations
- [ ] UX improvements