import random
import praw
from xml.etree.ElementTree import tostring
from discord.ext import commands
import json


# Cog for images from reddit



class RedditImages(commands.Cog):
    print("Initializing RedditImages Cog")
    def __init__(self, bot):
        self.bot = bot

    
        with open("key.json","r") as file:
            jsonData = json.load(file)
        self.key = jsonData["key"]
        REDDIT_APP_ID=jsonData["REDDIT_APP_ID"]
        REDDIT_APP_SECRET=jsonData["REDDIT_APP_SECRET"]
        REDDIT_USER=jsonData["username"]
        REDDIT_PASSWORD=jsonData["password"]
        

        # Praw init
        self.reddit = praw.Reddit(
            client_id= REDDIT_APP_ID,
            client_secret= REDDIT_APP_SECRET,
            password=REDDIT_PASSWORD,
            user_agent="Cheese.pyDiscord:%s:1.0" % REDDIT_APP_ID,
            username=REDDIT_USER,
        )


    # Bunny Reddit
    @commands.hybrid_command(aliases=['bun'])
    async def bunny(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("Rabbits").hot()

                        post_to_pick = random.randint(1,100)

                        for i in range(0, post_to_pick):
                            submission = next(x for x in submissions if not x.stickied)
                            ## print(submission.url)
                        if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                            notImage = False
                            break
                    await ctx.send(submission.url)
                    num = num - 1
            else:
                await ctx.send("This is not working, contact dev")


    # Minecraft Reddit
    @commands.hybrid_command(aliases=['mc'])
    async def minecraft(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("Minecraft").hot()

                        post_to_pick = random.randint(1,100)

                        for i in range(0, post_to_pick):
                            submission = next(x for x in submissions if not x.stickied)
                            ## print(submission.url)
                        if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                            notImage = False
                            break
                    await ctx.send(submission.url)
                    num = num - 1
            else:
                await ctx.send("This is not working, contact dev")

    # Meme Reddit
    @commands.hybrid_command(aliases=['m'])
    async def meme(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("memes").hot()

                        post_to_pick = random.randint(1,100)

                        for i in range(0, post_to_pick):
                            submission = next(x for x in submissions if not x.stickied)
                            ## print(submission.url)
                        if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                            notImage = False
                            break
                    await ctx.send(submission.url)
                    num = num - 1
            else:
                await ctx.send("This is not working, contact dev")


    # Cat Reddit
    @commands.hybrid_command(aliases=['kitty'])
    async def cat(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("cats").hot()

                        post_to_pick = random.randint(1,100)

                        for i in range(0, post_to_pick):
                            submission = next(x for x in submissions if not x.stickied)
                            ## print(submission.url)
                        if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                            notImage = False
                            break
                    await ctx.send(submission.url)
                    num = num - 1
            else:
                await ctx.send("This is not working, contact dev")

    # Dog Reddit
    @commands.hybrid_command(aliases=['doggo', 'doggy'])
    async def dog(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("dog").hot()

                        post_to_pick = random.randint(1,100)

                        for i in range(0, post_to_pick):
                            submission = next(x for x in submissions if not x.stickied)
                            ## print(submission.url)
                        if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                            notImage = False
                            break
                    await ctx.send(submission.url)
                    num = num - 1
            else:
                await ctx.send("This is not working, contact dev")


    def getKey(self):
        return self.key
    print("Finished Initializing RedditImages Cog")