import discord
from discord.ext import commands

class Role(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def addrole(self, ctx, role= discord.Role, user = discord.Member):
        if ctx.author.guild_permissions.administrator:
            await user.add_role(role)
            await ctx.send(f'Given {role.mention} to {user.mention}!')
    
    @commands.command()
    async def removerole(self, ctx, role= discord.Role, user = discord.Member):
        if ctx.author.guild_permissions.administrator:
            await user.remove_role(role)
            await ctx.send(f'Removed {role.mention} to {user.mention}!')


def setup(client):
    client.add_cog(Role(client))