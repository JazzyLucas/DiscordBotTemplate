async def handle_on_ready(client):
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    MY_GUILD = client.get_guild(int(client.MY_GUILD))
    client.tree.copy_global_to(guild=MY_GUILD)
    await client.tree.sync(guild=MY_GUILD)
    print('------')


def register_core_events(client):
    @client.event
    async def on_ready():
        await on_ready(client)
