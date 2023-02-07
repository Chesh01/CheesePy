import discord
from discord.ext import commands
from discord import app_commands


class Util(commands.Cog):
    print("Initializing Util Cog")
    def __init__(self, bot):
        self.bot = bot



    # Avatar command
    @commands.command(aliases= ["av"])
    async def avatar(self, ctx, *,member: discord.Member=None):
        member = ctx.author if not member else member
        embed = discord.Embed(title=member.name)
        embed.set_image(url=member.display_avatar)
        await ctx.send(embed=embed)


    # Banner Command
    @commands.command()
    async def banner(self, ctx, *,member: discord.Member=None):
        target = ctx.author or member
        fetched = await bot.fetch_user(target.id)
        # print(fetched.banner.url)
        embed = discord.Embed(title=fetched.name)
        embed.set_image(url=fetched.banner)
        await ctx.send(embed=embed)


    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.send(str(round(self.bot.latency*100.0, 2)) + "ms")

    # Tells Join Date of User
    @commands.hybrid_command(name="joined")
    async def joined(self, ctx, *, member: discord.Member=None):
        target = member or ctx.author
        await ctx.send(discord.utils.format_dt(target.joined_at, 'R'))



    @commands.hybrid_command(name="created")
    async def created(self, ctx, *, member: discord.Member=None):
        target = member or ctx.author
        await ctx.send(discord.utils.format_dt(target.created_at, 'R'))

    print("Finished Initializing Util Cog")