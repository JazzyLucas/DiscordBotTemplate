import discord
from discord import app_commands
from utils.discord_utils import connect_to_discord
from utils.config_util import load_config
from cogs.basic_commands import register_commands

##################################################
##### Initialization
##################################################

##### Config
config = configparser.ConfigParser(interpolation=None)
config.read('config.txt')
DISCORD_TOKEN = config['DISCORD']['TOKEN']
MY_GUILD = discord.Object(config['DISCORD']['GUILD_ID'])


##### Discord
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = MyClient(intents=intents)

##################################################
##### LOGIC
##################################################


def send_ping_message(message="Pong!"):
    # Some logic here
    return message


##################################################
##### COMMANDS
##################################################

@client.tree.command()
async def ping(interaction: discord.Interaction, message: str):
    """Let's see if the bot is alive!"""
    await interaction.response.defer(ephemeral=True)
    await interaction.followup.send(content=send_ping_message(message))


##################################################
##### EVENTS
##################################################

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


connect_to_discord(client, DISCORD_TOKEN)
