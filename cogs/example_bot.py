import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands

from ManagerSan import *

client = discord.Client()
bot = commands.Bot(command_prefix='uwu')

manager = ManagerSan()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('hello'):
#         await message.channel.send('Hello!')

#     if message.content.startswith('f'):
#         await message.channel.send('f u too')

#     logic(message)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Bot Is Online')

    # if ManagerSan exists, read

    # else create new ManagerSan

@bot.event
async def on_message(message): 
    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        # await message.channel.send('Hello!')
        await bot.send_message(message.channel, 'Hello!')

    if message.content.startswith('f'):
        await message.channel.send('f u too')
        # await bot.send_message(message.channel, 'Hello!')

    if message.content.startswith('ManagerSan'):
        args = message.content.split(' ')[1:]
        manager.process(args)

        # update project statuses in appropriate  
        await message.channel.send(str(manager))

    # logic(message)
    
# client.run(str(os.environ.get('TOKEN')))

bot.run(str(os.environ.get('TOKEN')))
