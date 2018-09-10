import discord
import random
import asyncio
from discord.ext import commands

dMember = discord.Member

class Admincmds:
    def __init__(self, bot):
        bot.self = bot


    async def on_ready(self):
        print("Administrative Commands Cog was loaded successfully!")


    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=30, max=250):
        sender = ctx.message.author
        if amount > max:
            await ctx.send("{} || Failed to clear messages! **(The max amount of messages you can clear is {}!)**".format(sender.mention, max))
        else:
            if amount == 1:
                await ctx.channel.purge(limit=amount)
                await asyncio.sleep(1)
                await ctx.send("{} || Sucessfully cleared **1** message.".format(sender.mention))
            else:
                await ctx.channel.purge(limit=amount)
                await asyncio.sleep(1)
                await ctx.send("{} || Sucessfully cleared **{}** messages.".format(sender.mention, amount))

    @clear.error
    async def clear_handler(self, ctx, error):
        sender = ctx.message.author
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} || Failed to clear messages! **(You don't have permissions to use this command!)**".format(sender.mention))


    @commands.command()
    async def info(self, ctx, user: discord.Member):
        embed = discord.Embed(title="User info", color=0xff5357)
        embed.add_field(name="Name", value="{}".format(user.name), inline=False)
        embed.add_field(name="Name on server", value="{}".format(user.display_name), inline=False)
        embed.add_field(name="ID", value="{}".format(user.id), inline=False)
        embed.add_field(name="Status", value="{}".format(user.status), inline=False)
        embed.add_field(name="Playing/Activity", value="{}".format(user.activity), inline=False)
        embed.add_field(name="Join Date", value="{}".format(user.joined_at), inline=False)
        embed.add_field(name="Highest Role", value="{}".format(user.top_role), inline=False)
        embed.add_field(name="Account Created", value="{}".format(user.created_at), inline=False)
        await ctx.send(embed=embed)

    @info.error
    async def info_handler(self, ctx, error):
        if error.param.name == 'user':
            await ctx.send("{} || Which user did you want to get the info of?".format(ctx.message.author.mention))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: dMember):
        sender = ctx.message.author
        if user.id == discord.Guild.owner_id:
            print("Server owner's id is {}".format(discord.Guild.owner_id))
            print("User's ID is {}".format(user.id))
            await ctx.send("{} || Not even I have the ability to kick the owner".format(sender.mention))
        else:
            if sender.top_role < user.top_role:
                await ctx.send("{} || Can't kick a role that's higher than yours!".format(sender.mention))
            else:
                if sender == user:
                    await ctx.send("{} || You can't kick yourself!".format(sender.mention))
                else:
                    await ctx.send("{} || Sucessfully kicked **{}**".format(sender.mention, user))
                    await dMember.kick(user, reason=None)

    @kick.error
    async def kick_handler(self, ctx, error):
        sender = ctx.message.author
        if error.param.name == 'user':
            await ctx.send("{} || You need to mention someone to kick.".format(sender.mention))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} || You don't have the permissions to use that command!".format(sender.mention))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: dMember, *, banReason):
        sender = ctx.message.author
        if user.id == discord.Guild.owner_id:
            print("Server owner's id is {}".format(discord.Guild.owner_id))
            print("User's ID is {}".format(user.id))
            await ctx.send("{} || Not even I have the ability to ban the owner".format(sender.mention))
        else:
            if sender.top_role < user.top_role:
                await ctx.send("{} || Can't ban a role that's higher than yours!".format(sender.mention))
            else:
                if sender == user:
                    await ctx.send("{} || You can't ban yourself!".format(sender.mention))
                else:
                    await ctx.send("{} || Sucessfully banned **{}** for {}".format(sender.mention, user, banReason))
                    await dMember.ban(user, reason=banReason)

    @ban.error
    @commands.has_permissions(ban_members=True)
    async def ban_handler(self, ctx, error):
        sender = ctx.message.author
        if error.param.name == 'user':
            await ctx.send("{} || You need to mention someone to ban.".format(sender.mention))
        if error.param.name == 'banReason':
            await ctx.send("{} || You need to give a reason to ban that user.".format(sender.mention))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} || You don't have the permissions to use that command!")

def setup(bot):
    bot.add_cog(Admincmds(bot))