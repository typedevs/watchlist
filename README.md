# Watchlist

## Build
### Requirements
- [Docker](https://docs.docker.com/engine/install/debian/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Just](https://github.com/casey/just)

### Recipes
```sh
just --list        # Lists available recipes
just up            # Starts the application
just build         # Builds the application
just db            # Populate db
just deps          # Install dependencies on the local Python environment
```
