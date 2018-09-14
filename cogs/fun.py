
import json
memedata = json.load(open("config/reddit_data.json"))


#----------IMPORTS---------------
import discord
import random
import praw
from discord.ext import commands
#--------------------------------

class Fun:
    def __init__(self, bot):
        self.bot = bot


    async def on_ready(self):
        print("Fun Commands Cog was loaded successfully!")


    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        # Array used to get a random hugging gif from the images\hugging_gifs folder.
        hugginggifs = [
            discord.File('images/hugging_gifs/d69b8ce822eac0d007aeeb26228e8a50.gif'),
            discord.File('images/hugging_gifs/hugtime.gif'),
            discord.File('images/hugging_gifs/RevolvingWigglyDikkops-size_restricted.gif'),
            discord.File('images/hugging_gifs/Tumblrshit.gif'),
            discord.File('images/hugging_gifs/V47M1S4.gif'),
            discord.File('images/hugging_gifs/F2805f274471676c96aff2bc9fbedd70.gif')
        ] # (I'll probably switch this to a file hosting of some sort to make this easier)

        await ctx.send("{} gave ".format(ctx.message.author.mention) + "{} a hug! \n".format(user.mention))
        await ctx.send(file=random.choice(hugginggifs)) # Randomly picks a hugging gif from said array.


    @hug.error # Error handling
    async def hug_handler(self, ctx, error):
        if error.param.name == 'user': # Finds the missing parameter (argument) of your command.
            await ctx.send("{} gave... Hang on a minute, I think you forgot to mention someone to hug.".format(ctx.message.author.mention))


    @commands.command(aliases=['8ball']) # Pretty striaghtforward, makes it to where the command can be ran using $8ball intead of $eightball
    async def eightball(self, ctx, args):
        possibleresponses = [
            "Yes.",
            "Sure, why not?",
            "Without a doubt B)",
            "You may rely on it.",
            "Yeah, probably.",
            "I don't feel like answering right now. Try again later.",
            "Cannot predict now.",
            "Buzz off.",
            "Fuck no!",
            "Nope!",
            "My reply is no.",
            "My sources say no, and fuck off.",
            "Very doubtful."
        ]

        await ctx.send("{} :8ball: || ".format(ctx.message.author.mention) + random.choice(possibleresponses))

    @eightball.error
    async def eightball_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'args':
                await ctx.send("{} :8ball: || You need to ask a question. Any question!".format(ctx.message.author.mention))


    @commands.command()
    async def meme(self, ctx): # Reddit, now this is gonna get interesting.

        meme_subreddits = [
            'me_irl',
            'dankmemes'
        ]

        reddit = praw.Reddit(client_id=memedata['clientid'],
                             client_secret=memedata['clientsecret'],
                             user_agent=memedata['useragent']) # I put something in the readme.md to explain this bit.
        memes_submissions = reddit.subreddit(random.choice(meme_subreddits)).hot() # Picks a post from the 'hot' category of a subreddit.
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)


        embed = discord.Embed(title='Fresh memes hot and ready!', color=0xff6767)
        embed.set_image(url=submission.url) # This makes the image of the reddit post appear on the embed.
        embed.set_footer(text='Straight from a random subreddit!')

        await ctx.send(embed=embed)


    @commands.command(aliases=['f', 'F'])
    async def ftopayrespects(self, ctx):
        sender = ctx.message.author
        hearts = [
            ':heart:',
            ':purple_heart:',
            ':blue_heart:',
            ':green_heart:'
        ]
        await ctx.send("{} Has paid their respects {}".format(sender.mention, random.choice(hearts)))


    @commands.command()
    async def pinged(self, ctx):
        await ctx.send(file=discord.File('images/Tenor.gif'))


    @commands.command()
    async def gladward(self, ctx):
        await ctx.send(file=discord.File('images/gladward.png'))
        await ctx.send("G L A D W A R D")

#Adds the cog to the bot.
def setup(bot):
    bot.add_cog(Fun(bot))