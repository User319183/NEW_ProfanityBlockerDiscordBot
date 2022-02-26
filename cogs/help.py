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

import random
import uuid

from discord.commands import slash_command # Importing the decorator that makes slash commands.







class Help_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot






	@slash_command(name="help", description="Default help panel")
	async def help(self, ctx):
		
            embed=discord.Embed(title="Help Panel", color=0xD708CC, description = "The command you need for help.", url="https://discord.gg/ecz2z36gkB")
            embed.add_field(name = "Commands", value = f"__1. info__ \n __2. helpme__ \n __3. bypass__ \n __4. unbypass__ \n ")
            embed.add_field(name = "Our Website", value = "https://profanityblocker.org")
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)












	@slash_command(name="helpme", description="A helpme command")
	@commands.has_guild_permissions(administrator=True)
	@commands.cooldown(1, 120, commands.BucketType.guild)
	async def helpme(self, ctx, reason: Option(str, "Specify why you need help.")):
        
            
                if len(reason) > 50:
                    await ctx.respond("Reason must be lower than 30 characters! Try again in two minutes (120 seconds). ", ephemeral=True) 
                    
                else:
                    
                    embed = discord.Embed(title="Helpme", color=0xD708CC, description=f"```Your server invite has been created. A staff member or developer will join your server shortly.```")
                    embed.add_field(name = "Your Code", value = f" ```{uuid.uuid1()}``` ")
                    embed.add_field(name = "What is the code for?", value = f" In order for us to verify your issue you must send us your code. ")
                    embed.timestamp = discord.utils.utcnow() 
                    await ctx.respond(embed=embed)
                    invite = await ctx.channel.create_invite()


                    channel = self.bot.get_channel(872858303804350464)

                    total_users = len(ctx.guild.members)
                    total_bots = len([member for member in ctx.guild.members if member.bot == True])
                    total_humans = total_users - total_bots

                    e = discord.Embed(title="Helpme command used!", color= 0xD708CC)
                    e.add_field(name="Code", value = f" ```{uuid.uuid1()}``` ")
                    e.add_field(name="Reason", value = f" ```{reason}``` ")
                    e.add_field(name="Server Name:", value=ctx.guild.name, inline=False)
                    e.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
                    e.add_field(name="Guild Owner", value=str(ctx.guild.owner), inline=False)
                    e.add_field(name="Guild Users", value="{}".format(total_users))
                    e.add_field(name="Humans", value=total_humans)
                    e.add_field(name="Bots", value=total_bots)
                    e.add_field(name="Invite", value=invite)
                    try:
                        e.set_thumbnail(url=ctx.guild.icon.url)

                    except:
                        pass

                    try:
                        e.add_field(name="Roles", value=", ".join([str(r) for r in ctx.guild.roles]))

                    except:
                        pass

                    e.timestamp = datetime.utcnow()

                    await channel.send(embed=e)





















	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Help_Commands" has been loaded!')
		print(f'---------------------------------------')


def setup(bot):
	bot.add_cog(Help_Commands(bot))
	
