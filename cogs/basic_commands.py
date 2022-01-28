import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

import re
import string


from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from datetime import datetime


import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
from discord.commands import slash_command

import random
import uuid

import psutil




class Basic_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	@slash_command(name="debug", description="Debug the bot to get it's permissions that are enabled and disabled.")
	async def debug(self, ctx):
            
            if ctx.guild is None:
                embed = discord.Embed(title="A slash command error occured.", description=f"This slash command can't be used inside a DM.", color=0xD708CC)
                embed.timestamp = datetime.utcnow()
                await ctx.respond(embed=embed)


            else:
                embed = discord.Embed(title="Permissions", description=f"{dict(ctx.me.guild_permissions)}", color=0xD708CC)
                embed.timestamp = datetime.utcnow()
                await ctx.respond(embed=embed)



	@slash_command(name="info", description="Information about this bot")
	async def info(self, ctx):
            
            self.bot_embed_guilds = []

            for t in self.bot.guilds:
                self.bot_embed_guilds.append(t)
            embed = discord.Embed(title="Bot Info", description="General information about Profanity Blocker", color=0xD708CC)
            embed.add_field(name="__Bot developers:__", value="User319183#3149\n TheWizz1338#6367", inline=True)
            embed.add_field(name="__Server Count:__", value=f"{len(self.bot_embed_guilds)}", inline=True)
            embed.add_field(name="__Websocket Ping:__", value=f"{round(self.bot.latency * 1000)}")
            embed.add_field(name="__CPU Usage:__", value = f'{psutil.cpu_percent()}%', inline = False)
            embed.add_field(name="__Memory Usage:__", value = f'{psutil.virtual_memory().percent}%', inline = False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text = "https://profanityblocker.org")
            await ctx.respond(embed=embed)




	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Basic_Commands" has been loaded!')
		print(f'---------------------------------------')


def setup(bot):
	bot.add_cog(Basic_Commands(bot))