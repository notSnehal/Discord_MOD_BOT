import discord
import random
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle


client = commands.Bot(command_prefix = '.')
status = cycle(['Status 1', 'Status 2'])

@client.event
async def on_command_erro(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'You dont have the required permissions.')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass all the required arguments.')

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online.")

@client.event 
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "new role") 
    await ctx.add_roles(role)

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Test')
    await client.add_roles(member, role)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')









































client.run('ODM1MTEzNDAxNDIwMjE4Mzc4.YIKt9g.L1FHDUvM5U_yDs8hnOsC6FL0DTk')
