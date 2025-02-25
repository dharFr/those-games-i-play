# Backend Architecture

## Overview
The backend follows a layered architecture pattern with clear separation of concerns. Each layer has specific responsibilities and communicates only with adjacent layers.

```
┌──────────────────┐
│     API Layer    │ FastAPI routes, request/response models
├──────────────────┤
│  Service Layer   │ Business logic, recommendations, similarity
├──────────────────┤
│ Repository Layer │ Data access, caching strategy
└──────────────────┘
```

## Directory Structure
```
backend/
├── app/
│   ├── api/           # API routes and endpoints
│   │   ├── v1/        # API version 1
│   │   └── deps.py    # Dependency injection
│   ├── core/          # Core application code
│   │   ├── config.py  # Configuration management
│   │   └── errors.py  # Custom exceptions
│   ├── models/        # Pydantic models
│   │   ├── domain/    # Domain models
│   │   └── api/       # Request/Response models
│   ├── services/      # Business logic layer
│   │   ├── games.py   # Game-related operations
│   │   └── recommender.py
│   ├── repositories/  # Data access layer
│   │   ├── games.py   # Game data operations
│   │   └── cache.py   # Caching logic
│   └── steam/         # Steam API integration
└── tests/            # Test directory mirrors app structure
```

## Key Components

### 1. API Layer (FastAPI Routes)
- Handles HTTP requests/responses
- Input validation
- Authentication (future)
- Rate limiting (future)
- Response formatting

### 2. Service Layer
- Business logic
- Recommendation algorithms
- Similarity calculations
- Data transformation
- No direct data access

### 3. Repository Layer
- Data access abstraction
- Caching strategy
- Database operations
- External API calls (Steam)

## Data Flow Example
For a game search request:
```
1. HTTP Request
   └─► API Route (/games)
       └─► GameService
           ├─► GameRepository (DB check)
           │   └─► Redis Cache
           └─► SteamClient (if needed)
```

## Key Design Decisions

### Caching Strategy
- Redis for:
  - Frequently accessed game details
  - Search results
  - Similarity graphs
- Cache invalidation on game updates
- TTL-based expiration for Steam data

### Data Consistency
- MongoDB as source of truth
- Write-through caching
- Periodic Steam data sync

### Performance Considerations
- Paginated responses
- Eager loading of common data
- Background tasks for heavy operations
- Query optimization with proper indexes

### Error Handling
- Centralized error handling
- Custom exception classes
- Proper error propagation
- Detailed logging

## Implementation Phases

1. **Foundation** (Current)
   - Basic CRUD operations
   - Steam API integration
   - Data models

2. **Core Features**
   - Search and filtering
   - Basic similarity
   - Simple recommendations

3. **Advanced Features**
   - Graph relationships
   - Advanced recommendations
   - Caching optimization

4. **Optimization**
   - Performance tuning
   - Advanced caching
   - Monitoring
