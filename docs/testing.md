# API Testing Commands

## Games Endpoint

### List Games (default pagination)
```bash
curl -X GET "http://localhost:8000/api/v1/games" | jq
```

### List Games (custom page size)
```bash
curl -X GET "http://localhost:8000/api/v1/games?limit=5" | jq
```

### List Games (specific page)
```bash
curl -X GET "http://localhost:8000/api/v1/games?page=2&limit=10" | jq
```

### Test Invalid Parameters
```bash
# Test exceeding max page size
curl -X GET "http://localhost:8000/api/v1/games?limit=200" | jq

# Test invalid page number
curl -X GET "http://localhost:8000/api/v1/games?page=0" | jq
```

Note: The `jq` command is used to format the JSON output. If you don't have it installed, you can omit `| jq` from the commands.
