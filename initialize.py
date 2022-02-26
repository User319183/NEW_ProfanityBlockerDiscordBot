import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

from discord.ext import *
from discord.ext.commands import *
from ctypes import *
import datetime



import aiohttp
from contextlib import redirect_stdout

import random
import uuid













if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]


























































intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False
intents.members = True
# intents.reactions = True



bot = commands.Bot(command_prefix="pb-", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=f"for profanity"))

bot.remove_command('help')

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")


@bot.listen()
async def on_ready():
    print(f'Bot has been activated! Modules loaded.')
    print(f'---------------------------------------')
    
    








@bot.listen()
async def on_guild_join(guild):
    channel = bot.get_channel(888570275426340905)

    total_users = len(guild.members)
    total_bots = len([member for member in guild.members if member.bot == True])
    total_humans = total_users - total_bots

    e = discord.Embed(title="I've joined a server.", color= 3447003)
    e.add_field(name="Server Name:", value=guild.name, inline=False)
    e.add_field(name="Guild ID", value=guild.id, inline=False)
    e.add_field(name="Guild Owner", value=str(guild.owner), inline=False)
    e.add_field(name="Guild Users", value="{}".format(total_users))
    e.add_field(name="Humans", value=total_humans)
    e.add_field(name="Bots", value=total_bots)
    try:
        e.set_thumbnail(url=guild.icon.url)

    except:
        pass

    e.timestamp = datetime.datetime.utcnow()

    await channel.send(embed=e)





#find remove guild
@bot.listen()
async def on_guild_remove(guild):
    channel = bot.get_channel(888570303930839100)


    total_users = len(guild.members)
    total_bots = len([member for member in guild.members if member.bot == True])
    total_humans = total_users - total_bots

    e = discord.Embed(title="I've left a server.", color=15158332)
    e.add_field(name="Server Name:", value=guild.name, inline=False)
    e.add_field(name="Guild ID", value=guild.id, inline=False)
    e.add_field(name="Guild Owner", value=str(guild.owner), inline=False)
    e.add_field(name="Guild Users", value="{}".format(total_users))
    e.add_field(name="Humans", value=total_humans)
    e.add_field(name="Bots", value=total_bots)
    try:
        e.set_thumbnail(url=guild.icon.url)

    except:
        pass

    e.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=e)


















bot.run(token)
