import discord
from discord.ext import commands

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'banned {member.mention}')
        
    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You dont have the required permission.')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please pass all the required arguments.')


    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You dont have the required permissions.')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please mention the member along with the #.')
        
def setup(client):
    client.add_cog(Ban(client))