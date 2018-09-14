# Gladward Version 1
A bot made in the discord.py rewrite.

## What even is gladward?
Gladward is an open source bot made by Zeexel in the discord.py rewrite. While it's not completely done, there's still many things to play around with at the moment.


## Why the hell should I put this piece of crap in my server?
Why not? It may not be the best bot, but it's still a bot.

## What kinda features are planned to come in the near future?

### Lockdown
Locks all channels down in case of a raid and prevents new users from joining until the lockdown is disabled.
### Logging
Logs certain actions based on the user's specifications.
### User-Suggested features.
Features that users suggest in the support discord.

# Things you should probably know if you're gonna use this as a base for your bot.
(Hey you should probably credit me when you use this code)

## What do I need to use this?
You need the discord.py rewrite, which can be downloaded here:
https://github.com/Rapptz/discord.py/tree/rewrite
(If you don't feel like finding the command yourself, here.)
pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]

You also need praw 6.0.0, which can be installed by using this command on your terminal: pip install praw


### Reddit instructions (For the memes command and the nsfw commands)
Go to https://www.reddit.com/prefs/apps/

Click "Create App" (or in some cases 'Create Another App')
You should see this. Make a name for it and a description.
![B)](https://i.imgur.com/75NDvP2.png)

Next, change this to be a script intended for personal use.
![NO COOL DUDES, VERY ILLEGAL!](https://i.imgur.com/mSZmRs5.png)

Finally, make a file in your config (if you're using one) called reddit_data.json (or whatever you want)
Make sure it looks like this (again, make the variable names whatever)

![B)](https://imgur.com/2Q5iWzz.png)

Put your client id, secret, and user agent (which is just the name of your application) into these variables.

## Using it in the bot

Make sure you have json imported, and your json file is loaded in the cog.
![B)](https://imgur.com/JNVfoZS.png)

(Also might wanna make sure you have praw imported here because reddit)

Next, use the variables defined in the json file with your python script like this.
![](https://imgur.com/pGiEf5t.png)

## And after all that, your bot should be done!

![Heyy, that's pretty good!](https://imgur.com/HXkqdDp.png)


### Reminder:
Please don't contact me for issues regarding discord.py, that should be taken to the ![discord.py server](https://discordapp.com/invite/r3sSKJJ), which has support for both the rewrite and the asyncio (0.16.x) versions. 



