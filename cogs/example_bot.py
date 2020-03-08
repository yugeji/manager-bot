import discord
from private_config import token
from utils import logic

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('f'):
        await message.channel.send('f u too')

    logic(message)


client.run(token)
