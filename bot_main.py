import discord
from discord import app_commands
from utils.config_utils import get_config_values
from utils.discord_utils import connect_to_discord
from cogs.basic_commands import register_commands
from events.core_events import handle_on_ready


# Discord Client Initialization
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.DISCORD_TOKEN, self.MY_GUILD = get_config_values('config.txt')


# Initialize client
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = MyClient(intents=intents)

# Register core events
handle_on_ready(client)


# Register commands
def register_all_commands(client):
    register_commands(client)
    # Add more command modules here as you create them


# Register all commands
register_all_commands(client)

# Connect to Discord
connect_to_discord(client, client.DISCORD_TOKEN)
