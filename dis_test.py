import discord
from discord.ext import commands
import os
import dis_helper

TOKEN = os.environ.get('discord_token')

client = commands.Bot(command_prefix = '$')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! (round(client.latency*1000))ms')


# https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
@client.command()
async def bs(ctx, arg):
    await ctx.send(arg)
    bs = arg.strip()
    dis_helper.sqlite_create_table()
    dtstmp = dis_helper.return_date()
    new_row = dis_helper.reads_in_bs(bs)
    dis_helper.sqlite_data_entry(new_row)
    
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)

