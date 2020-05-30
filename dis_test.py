# Work with Python 3.6
import discord
from discord.ext import commands

TOKEN = 'NzEyNzg2NjQ5NjI4ODAzMTUx.Xsn48A.SImmoUH4xPelhcLhKJtyhACsIQ4'

client = commands.Bot(command_prefix = '.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! (round(client.latency*1000))ms')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

