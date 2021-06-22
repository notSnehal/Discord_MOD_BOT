import discord
from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    
    
class ReactionRolesNotSetup(commands.CommandError):
    '''Reaction Roles are not setup for this guild.'''
    pass

def is_setup():
    async def warp_func(ctx):
        data = await ctx.bot.config.find(ctx.guild.id)



    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined the server!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server!")

    
    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def whois(self, ctx, member : discord.Member):
        embed = discord.Embed(title = member.name, description=member.mention, color = discord.Colour.green())
        embed.add_field(name = "ID", value = member.id, inline=True)
        embed.add_field(name = "Role", value = member.top_role, inline=True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))