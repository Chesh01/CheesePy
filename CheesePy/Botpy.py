from multiprocessing.connection import Client
from wsgiref.util import application_uri
from xml.etree.ElementTree import tostring
import discord
from discord.ext import commands
from discord import app_commands
import json
from typing import Literal, Union, NamedTuple
from enum import Enum


from redditImages import RedditImages
from util import Util
from voice import *


import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')




intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix='$', intents=intents)






@bot.event
async def on_ready():
    print(f'Logging in')
    discord.utils.setup_logging()
    await bot.add_cog(RedditImages(bot))
    await bot.add_cog(Util(bot))
    await bot.add_cog(Music(bot))
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)



    print(f'We have logged in as {bot.user}')


async def on_message_delete(self, message):
    msg = f'{message.author} has deleted the message: {message.content}'
    await message.channel.send(msg)
    print("msg")



#No
@bot.hybrid_command()
async def porn(ctx):
    await ctx.send("No.")

# Ci
@bot.command()
async def ci(ctx):
    await ctx.send("Is amazing")







'''with open("./cfg/keyPy.json","r") as file:
    jsonData = json.load(file)
key = jsonData["key"]
# print(key)'''
keyGrab = RedditImages(bot)
key = str(RedditImages.getKey(keyGrab))
print(key)
bot.run(key) #, log_handler=handler)