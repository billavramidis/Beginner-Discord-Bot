from disnake.ext import commands
import random

class Misc(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name = "hi",
        description = "Greets the member.",
    )
    async def hi(ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.slash_command(
        name = "roll", 
        description = "Rolls a dice.",
    )
    async def roll(ctx):
        dice = random.randint(1,6)
        await ctx.send(f"You rolled a {dice}!")

    @commands.slash_command(
        name = "iq", 
        description = "Tells you how much IQ you have.",
    )
    async def iq(ctx):
        iq = random.randint(0,250)
        await ctx.send(f"{ctx.author.name} you have {iq} IQ.")

    @commands.slash_command(
        name = "gay", 
        description = "Tells you how gay you are.",
    )
    async def gay(ctx):
        gay_rate = random.randint(0,100)
        await ctx.send(f"{ctx.author.name} you are {gay_rate}% gay.")

def setup(bot):
    bot.add_cog(Misc(bot))