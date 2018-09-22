import discord
from discord.ext import commands
invlink = 'https://discordapp.com/oauth2/authorize?client_id=482645162032365568&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2F&response_type=code&scope=identify%20bot'
serverlink = 'https://discord.gg/YwKsKW'

class General:
    def __init__(self, bot):
        bot.self = bot



    async def on_ready(self):
        print("General Commands Cog was loaded sucessfully!")

    @commands.command()
    async def server(self, ctx):
        sender = ctx.message.author
        await ctx.send("{} || {}".format(sender.mention, serverlink))

    @commands.command()
    async def invite(self, ctx):
        sender = ctx.message.author
        await ctx.send("{} || {}".format(sender.mention, invlink))



    @commands.command()
    async def uptime(self, ctx):
        bot = ctx.bot
        await ctx.send(bot.uptime)

    @commands.command()
    async def ping(self, ctx):
        bot = ctx.bot
        await ctx.send("Pong! :ping_pong: **({} ms)**".format(round(bot.latency)))

def setup(bot):
    bot.add_cog(General(bot))