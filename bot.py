#Gladward Bot Verson 0.0.1A
#(C) Zeexel 2018

#This script is just the initalization and where it adds all of the cogs. Most of the actual commands are in the "cogs" folder.



# Loads the config file
import json
config = json.load(open("config/settings.json","r"))
#---------------------------------------------------------------
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="g$")
bot.remove_command('help')
#---------------------------------------------------------------


#Should be pretty straightfoward, this is what should happen when the bot is turned on.

@bot.event
async def on_ready():
    game = discord.Game(name="g$help | Running in {} servers!".format(len(list(bot.guilds))))
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Ready for use!")
    print("Discord.py Version {}".format(discord.__version__))
    print("Logged in as:\n{}/{}#{}".format(bot.user.id, bot.user.name, bot.user.discriminator))
    print("Running in {} servers!".format(len(list(bot.guilds))))
    print("https://zeexel.github.io")
    print("|||||||||||||||||||||||||||||||||||||")

#Loads the cogs and then logs into the bot using the token given by the discord developers portal.

bot.load_extension("cogs.nsfw")
bot.load_extension("cogs.secret_commands")
bot.load_extension("cogs.help")
bot.load_extension("cogs.general")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.admincmds")
bot.run(config['token'])