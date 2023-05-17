from disnake.ext import commands
from tokens import joke_token
import requests
import random

class Misc(commands.Cog):
    def __init__(self, bot):
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

    @commands.slash_command(
        name = "rps",
        description = "Plays rock-paper-scissors with you."
    )
    async def rps(self, ctx):
        choices = ['rock', 'paper', 'scissors']
        await ctx.send("To play, please type rock/paper/scissors or exit to exit the game!")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        while True:
            message = await self.bot.wait_for('message', check = check)
            player_choice = message.content.lower()

            if player_choice == 'exit':
                await ctx.send("Exiting the game!")
                return
            
            if player_choice in choices:
                break

            await ctx.send("Please type rock/paper/scissors or exit to exit the game!")
        
        computer_choice = random.choice(choices).lower()

        if player_choice == computer_choice:
            await ctx.send(f"It's a tie! We both picked {computer_choice}.")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
            await ctx.send(f"You win! I picked {computer_choice}.")
        else:
            await ctx.send(f"I win! I picked {computer_choice}.")

    @commands.slash_command(name = "joke", description = "Tells a random joke.")
    async def joke(ctx):
    
        url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

        headers = {
            "X-RapidAPI-Key": joke_token,
            "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        joke = response.json()[0]['joke']
        
        await ctx.send(joke)


def setup(bot):
    bot.add_cog(Misc(bot))