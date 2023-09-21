import discord


def register_commands(client):
    @client.tree.command()
    async def ping(interaction: discord.Interaction, message: str):
        """Let's see if the bot is alive!"""
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(content="Pong!")