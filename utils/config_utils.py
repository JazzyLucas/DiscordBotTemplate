import os
import configparser
from typing import Tuple

def get_config(config_file_path: str) -> configparser.ConfigParser:
    """Load and return the configuration settings."""
    config = configparser.ConfigParser(interpolation=None)
    config.read(config_file_path)
    return config

def get_config_values(config_file_path: str) -> Tuple[str, str]:
    """Load and return Discord token and guild ID, with environment variable fallbacks."""
    # Determine if running in Docker
    in_docker = os.environ.get('IN_DOCKER', False)

    # Set the path to config.txt
    config_path = '/app/config.txt' if in_docker else config_file_path

    config = configparser.ConfigParser(interpolation=None)
    config.read(config_path)

    discord_token = config.get('DISCORD', 'TOKEN', fallback=os.environ.get('DISCORD_TOKEN'))
    discord_guild = int(config.get('DISCORD', 'GUILD_ID', fallback=os.environ.get('DISCORD_GUILD_ID')))

    return discord_token, discord_guild
