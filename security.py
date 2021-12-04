import os

OPEN_WEATHER_MAP_KEY = 'openweathermap'
SPOTIFY_CLIENT_ID_KEY = 'spotify_client_id'
SPOTIFY_CLIENT_SECRET_KEY = 'spotify_client_secret'
TELEGRAM_KEY = 'telegram'
DISCORD_KEY = 'discord'
DISCORD_CLIENT_ID_KEY = 'discord_client_id'
DISCORD_CLIENT_SECRET_KEY = 'discord_client_secret'

api_key = {
    OPEN_WEATHER_MAP_KEY: os.environ.get(OPEN_WEATHER_MAP_KEY),
    SPOTIFY_CLIENT_ID_KEY: os.environ.get(SPOTIFY_CLIENT_ID_KEY),
    SPOTIFY_CLIENT_SECRET_KEY: os.environ.get(SPOTIFY_CLIENT_SECRET_KEY),
    TELEGRAM_KEY: os.environ.get(TELEGRAM_KEY),
    DISCORD_KEY: os.environ.get(DISCORD_KEY),
    DISCORD_KEY: os.environ.get(DISCORD_KEY),
    DISCORD_CLIENT_ID_KEY: os.environ.get(DISCORD_CLIENT_ID_KEY),
    DISCORD_CLIENT_SECRET_KEY: os.environ.get(DISCORD_CLIENT_SECRET_KEY),
}