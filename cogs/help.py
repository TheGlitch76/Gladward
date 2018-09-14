import discord
from discord.ext import commands
import traceback
import sys

class HelpCmds:
    def __init__(self, bot):
        bot.self = bot



    async def on_ready(self):
        print("Help Command was loaded sucessfully!")


    @commands.command(aliases=['commands', 'hlp', 'cmds', 'Help'])
    async def help(self, ctx, page):
        if page == 'admin':
            embed = discord.Embed(title="Gladward Administrative Commands", color=0xff0023)
            embed.set_author(name="Zeexel made this", url="https://zeexel.github.io", icon_url="https://cdn.discordapp.com/attachments/474928804964597782/482649495776133130/Comm152.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452298699004182529/482649364871905290/image.png")
            embed.add_field(name="$clear/purge [amount]", value="``Purges messages in a channel with a limit of 250. Clears 30 messages by default.``", inline=False)
            embed.add_field(name="$kick [user]", value="``Kicks a specific user.``", inline=False)
            embed.add_field(name="$ban [user] [reason]", value="``Bans a specific user with a reason.``", inline=False)
            await ctx.send(embed=embed)
        if page == 'fun':
            embed = discord.Embed(title="Gladward Fun Commands", color=0x66ff1c)
            embed.set_author(name="Zeexel made this", url="https://zeexel.github.io", icon_url="https://cdn.discordapp.com/attachments/474928804964597782/482649495776133130/Comm152.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452298699004182529/482649364871905290/image.png")
            embed.add_field(name="$8ball/eightball [question]", value="``Ask a question and the magic 8-ball will answer!``", inline=False)
            embed.add_field(name="$hug [user]", value="``Hug literally anyone``", inline=False)
            embed.add_field(name="$meme", value="``Steals a meme from a random subreddit``", inline=False)
            embed.add_field(name="$pinged", value="``Use when someone makes a retarded ping``", inline=False)
            embed.add_field(name="$f", value="``Press F to pay respects.``", inline=False)
            embed.add_field(name="$gladward", value="``G L A D W A R D``", inline=False)
            await ctx.send(embed=embed)
        if page == 'nsfw':
            embed = discord.Embed(title="Gladward NSFW Commands ( ͡° ͜ʖ ͡°)", color=0xf449cd)
            embed.set_author(name="Zeexel made this", url="https://zeexel.github.io", icon_url="https://cdn.discordapp.com/attachments/474928804964597782/482649495776133130/Comm152.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452298699004182529/482649364871905290/image.png")
            embed.add_field(name="$hentai", value="``Grabs hentai straight off of r/hentai``", inline=False)
            embed.add_field(name="$loli", value="``If you use this command you're gay.``", inline=False)
            embed.add_field(name="$paizuri", value="``Grabs a paizuri straight off of r/paizuri``", inline=False)
            embed.add_field(name="$neko", value="``Grabs a neko straight off of r/nekogirls``", inline=False)
            embed.set_footer(text="These commands only work in NSFW channels")
            await ctx.send(embed=embed)
        if page == 'general':
            embed = discord.Embed(title="Gladward Bot Commands", color=0x5ec7ff)
            embed.set_author(name="Zeexel made this", url="https://zeexel.github.io", icon_url="https://cdn.discordapp.com/attachments/474928804964597782/482649495776133130/Comm152.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452298699004182529/482649364871905290/image.png")
            embed.add_field(name="$server", value="``Provides and invite link to Zeexel's server``", inline=False)
            embed.add_field(name="$invite", value="``Provides a link to invite gladward to your server!``", inline=False)
            embed.add_field(name="$ping", value="``Pongs right back at you, buddy.``", inline=False)
            await ctx.send(embed=embed)


    @help.error
    async def help_handler(self, ctx, error):
        if error.param.name == 'page':
            embed = discord.Embed(title="Gladward Bot Commands", color=0x5ec7ff)
            embed.set_author(name="Zeexel made this", url="https://zeexel.github.io", icon_url="https://cdn.discordapp.com/attachments/474928804964597782/482649495776133130/Comm152.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452298699004182529/482649364871905290/image.png")
            embed.add_field(name="Admin Commands", value="``$help admin``", inline=True)
            embed.add_field(name="Fun commands", value="``$help fun``", inline=True)
            embed.add_field(name="NSFW ( ͡° ͜ʖ ͡°)", value="``$help nsfw``", inline=True)
            embed.add_field(name="General Commands", value="``$help general``", inline=True)
            embed.set_footer(text="Version 0.0.1A | Made by Zeexel#2951")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCmds(bot))