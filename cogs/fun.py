import discord
import random
import traceback
import sys
import praw
from discord.ext import commands


class Fun:
    def __init__(self, bot):
        self.bot = bot


    async def on_ready(self):
        print("Fun Commands Cog was loaded successfully!")


    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        hugginggifs = [
            discord.File('images\hugging_gifs\d69b8ce822eac0d007aeeb26228e8a50.gif'),
            discord.File('images\hugging_gifs\hugtime.gif'),
            discord.File('images\hugging_gifs\RevolvingWigglyDikkops-size_restricted.gif'),
            discord.File('images\hugging_gifs\Tumblrshit.gif'),
            discord.File('images\hugging_gifs\V47M1S4.gif'),
            discord.File('images\hugging_gifs\F2805f274471676c96aff2bc9fbedd70.gif')
        ]
        await ctx.send("{} gave ".format(ctx.message.author.mention) + "{} a hug! \n".format(user.mention))
        await ctx.send(file=random.choice(hugginggifs))

    @hug.error
    async def hug_handler(self, ctx, error):
        if error.param.name == 'user':
            await ctx.send("{} gave... Hang on a minute, I think you forgot to mention someone to hug.".format(ctx.message.author.mention))

    @commands.command(aliases=['8ball'])
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
    async def meme(self, ctx):

        meme_subreddits = [
            'me_irl',
            'dankmemes'
        ]

        reddit = praw.Reddit(client_id='KIcJ2fQpsJpKZg',
                             client_secret='WpLetIWBxKwK_jyZUQkWU2PN-lA',
                             user_agent='Gladward')
        memes_submissions = reddit.subreddit(random.choice(meme_subreddits)).hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)


        embed = discord.Embed(title='Fresh memes hot and ready!', color=0xff6767)
        embed.set_image(url=submission.url)
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
        await ctx.send(file=discord.File('images\Tenor.gif'))


    @commands.command()
    async def gladward(self, ctx):
        await ctx.send(file=discord.File('images\gladward.png'))
        await ctx.send("G L A D W A R D")



def setup(bot):
    bot.add_cog(Fun(bot))