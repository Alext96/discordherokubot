import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
    print("Thanks for using bot")
    await client.change_presence(game=discord.Game(name="Baby Seal"))

@client.event
async def on_message(message):
    if message.content == "Hello":
        await client.send_message(message.channel, "World")
    if message.content.startswith(".hello"):
        msg = 'Good bye {0.author.mention} hope to see u again :wave:'.format(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))
