# API Specification

## Overview
This document describes the REST API endpoints for Those Games I Play application. The API follows OpenAPI standards and provides endpoints to list and retrieve game information.

## Design Rationale

### Core CRUD Operations (`/games`)
- **List Games (GET)**: 
  - Extensive filtering options support diverse discovery patterns
  - Pagination is crucial as the dataset will grow significantly
  - Sort options enable different browsing strategies (price-based, popularity-based)
  - Query parameters chosen over POST to enable caching and bookmarking

- **Game Details (GET)**:
  - Includes both basic and extended information in one call to reduce API requests
  - Similar games preview included to enable navigation paths
  - Screenshots and detailed metadata support rich game presentation

- **Create/Update Games (POST/PUT)**:
  - Full create/update support for future admin interface
  - Timestamps added for data freshness tracking
  - Conflict detection to maintain data integrity

### Graph & Relationships (`/games/{game_id}/graph`)
- Dedicated endpoint for visualization needs
- Query parameters control graph complexity:
  - `depth`: Controls how "far" from the original game to explore
  - `min_weight`: Filters weak relationships for clearer visualizations
  - `limit`: Prevents oversized graphs that could impact performance
- Node types (core/similar/related) enable visual hierarchy
- Edge types explain relationship nature (crucial for understanding connections)

### Recommendations (`/recommendations`)
- Flexible input parameters to support different recommendation scenarios:
  - Based on specific games (source_games)
  - Based on preferences (genres/tags)
  - Price-aware recommendations
- Includes explanation system for transparency
- Confidence scores help users evaluate suggestions
- Factors breakdown enables recommendation fine-tuning

### Similar Games (`/games/{game_id}/similar`)
- Separated from main game details for:
  - More detailed similarity metrics
  - Different filtering criteria
  - Potential for different caching strategies
- Multiple similarity metrics enable multi-faceted comparison
- Criteria parameter allows context-specific similarity focus

## Base URL
```
http://localhost:8000/api/v1
```

## Endpoints

### List Games
```http
GET /games
```

Returns a paginated list of games with filtering capabilities.

#### Query Parameters
| Parameter       | Type     | Default | Description                                    |
|----------------|----------|---------|------------------------------------------------|
| page           | integer  | 1       | Page number for pagination                     |
| limit          | integer  | 20      | Number of items per page (max: 100)           |
| genres         | string[] | null    | Filter by genres (comma-separated)            |
| tags           | string[] | null    | Filter by tags (comma-separated)              |
| price_min      | float    | null    | Minimum price filter                          |
| price_max      | float    | null    | Maximum price filter                          |
| released_after | date     | null    | Filter games released after date (YYYY-MM-DD) |
| released_before| date     | null    | Filter games released before date (YYYY-MM-DD)|
| sort_by        | string   | null    | Field to sort by (release_date, price, review_score) |
| sort_order     | string   | asc     | Sort order (asc, desc)                        |

#### Response
```json
{
  "items": [
    {
      "steam_id": 123456,
      "title": "Game Title",
      "genres": ["Indie", "Action"],
      "tags": ["Pixel Art", "2D"],
      "price": 19.99,
      "release_date": "2023-01-01",
      "review_score": 85,
      "review_count": 1000
    }
  ],
  "metadata": {
    "total_items": 150,
    "total_pages": 8,
    "current_page": 1,
    "items_per_page": 20
  }
}
```

### Get Game Details
```http
GET /games/{game_id}
```

Returns detailed information about a specific game.

#### Path Parameters
| Parameter | Type    | Description          |
|-----------|---------|---------------------|
| game_id   | integer | Steam ID of the game|

#### Response
```json
{
  "steam_id": 123456,
  "title": "Game Title",
  "genres": ["Indie", "Action"],
  "tags": ["Pixel Art", "2D"],
  "price": 19.99,
  "release_date": "2023-01-01",
  "review_score": 85,
  "review_count": 1000,
  "description": "Full game description...",
  "publisher": "Publisher Name",
  "developer": "Developer Name",
  "screenshots": ["url1", "url2"],
  "similar_games": [
    {
      "steam_id": 789012,
      "title": "Similar Game",
      "similarity_score": 0.85
    }
  ]
}
```

### Create Game
```http
POST /games
```

Creates a new game entry.

#### Request Body
```json
{
  "steam_id": 123456,
  "title": "Game Title",
  "genres": ["Indie", "Action"],
  "tags": ["Pixel Art", "2D"],
  "price": 19.99,
  "release_date": "2023-01-01",
  "review_score": 85,
  "review_count": 1000,
  "description": "Full game description...",
  "publisher": "Publisher Name",
  "developer": "Developer Name",
  "screenshots": ["url1", "url2"]
}
```

#### Response
```json
{
  "steam_id": 123456,
  "title": "Game Title",
  // ...other fields as in request...
  "created_at": "2023-11-15T10:30:00Z"
}
```

### Update Game
```http
PUT /games/{game_id}
```

Updates an existing game entry.

#### Path Parameters
| Parameter | Type    | Description          |
|-----------|---------|---------------------|
| game_id   | integer | Steam ID of the game|

#### Request Body
```json
{
  "title": "Updated Game Title",
  "genres": ["Indie", "Action"],
  "tags": ["Pixel Art", "2D"],
  "price": 24.99,
  "review_score": 87,
  "review_count": 1200
}
```

#### Response
```json
{
  "steam_id": 123456,
  "title": "Updated Game Title",
  // ...other updated fields...
  "updated_at": "2023-11-15T11:45:00Z"
}
```

### Get Game Relationship Graph
```http
GET /games/{game_id}/graph
```

Returns a graph of game relationships centered around the specified game.

#### Query Parameters
| Parameter    | Type    | Default | Description                                    |
|-------------|---------|---------|------------------------------------------------|
| depth       | integer | 2       | How many levels of relationships to include    |
| min_weight  | float   | 0.5     | Minimum similarity score to include (0.0-1.0)  |
| limit       | integer | 50      | Maximum number of nodes in the graph           |

#### Response
```json
{
  "nodes": [
    {
      "id": 123456,
      "title": "Game Title",
      "genres": ["Indie", "Action"],
      "type": "core"  // core, similar, or related
    }
  ],
  "edges": [
    {
      "source": 123456,
      "target": 789012,
      "weight": 0.85,
      "type": "genre_similarity"  // genre_similarity, tag_similarity, etc.
    }
  ]
}
```

### Get Recommendations
```http
GET /recommendations
```

Returns game recommendations based on specified criteria.

#### Query Parameters
| Parameter      | Type     | Default | Description                                     |
|---------------|----------|---------|-------------------------------------------------|
| source_games  | integer[]| null    | Steam IDs of games to base recommendations on   |
| genres        | string[] | null    | Preferred genres                                |
| tags          | string[] | null    | Preferred tags                                  |
| price_range   | string   | null    | Price range (e.g., "0-15", "15-30")            |
| limit         | integer  | 10      | Number of recommendations to return             |

#### Response
```json
{
  "recommendations": [
    {
      "steam_id": 123456,
      "title": "Game Title",
      "confidence_score": 0.92,
      "reason": "Similar to Game X, matches preferred genres",
      // ... other game fields
    }
  ],
  "explanation": {
    "factors": [
      {
        "type": "genre_match",
        "weight": 0.4
      },
      {
        "type": "similarity_to_played",
        "weight": 0.6
      }
    ]
  }
}
```

### Get Popular Similar Games
```http
GET /games/{game_id}/similar
```

Returns a curated list of similar games with similarity metrics.

#### Query Parameters
| Parameter    | Type     | Default | Description                                     |
|-------------|----------|---------|-------------------------------------------------|
| limit       | integer  | 10      | Number of similar games to return               |
| criteria    | string[] | all     | Similarity criteria (genres, tags, popularity)   |

#### Response
```json
{
  "similar_games": [
    {
      "steam_id": 789012,
      "title": "Similar Game",
      "similarity_metrics": {
        "genre_match": 0.8,
        "tag_match": 0.9,
        "price_range_match": 0.7,
        "overall_score": 0.85
      },
      // ... other game fields
    }
  ]
}
```

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "error": "Bad Request",
  "message": "Invalid parameter value",
  "details": {
    "parameter": "limit",
    "reason": "Must be between 1 and 100"
  }
}
```

### 404 Not Found
```json
{
  "error": "Not Found",
  "message": "Game not found"
}
```

### 409 Conflict
```json
{
  "error": "Conflict",
  "message": "Game with steam_id already exists",
  "details": {
    "steam_id": 123456
  }
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```
