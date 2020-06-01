# Work with Python 3.6
import discord
from discord.ext import commands
import os

TOKEN = os.environ.get('discord_token')

client = commands.Bot(command_prefix = '$')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! (round(client.latency*1000))ms')

def export_list(l):
    pass
    # https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
@client.command()
async def bs(ctx, arg):
    await ctx.send(arg)
    temp_list = []
    temp_list.append(arg.strip())
    print(temp_list)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)

