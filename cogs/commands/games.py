from disnake.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name = "rps",
        description = "Plays rock-paper-scissors with you."
    )
    async def rps(self, ctx):
        choices = ['rock', 'paper', 'scissors']
        await ctx.send("`To play, please type rock/paper/scissors or exit to exit the game!`")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        while True:
            message = await self.bot.wait_for('message', check = check)
            player_choice = message.content.lower()

            if player_choice == 'exit':
                await ctx.send("`Exiting the game!`")
                return
            
            if player_choice in choices:
                break

            await ctx.send("`Please type rock/paper/scissors or exit to exit the game!`")
        
        computer_choice = random.choice(choices).lower()

        if player_choice == computer_choice:
            await ctx.send(f"`It's a tie! We both picked {computer_choice}.`")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
            await ctx.send(f"`You win! I picked {computer_choice}.`")
        else:
            await ctx.send(f"`I win! I picked {computer_choice}.`")

    @commands.slash_command(
        name = "tictactoe",
        description = "You play Tic-Tac-Toe with someone."
    )
    async def tictactoe(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        await ctx.send("Welcome to Tic-Tac-Toe! To play mention an other server member!")
        message = await self.bot.wait_for("message", check=check)
        
        while True:
            if message.mentions:
                mentioned_user = message.mentions[0]
                original_user = ctx.user
                if mentioned_user == original_user:
                    await ctx.send("You can't mention yourself! Mention someone else to continue!")
                    message = await self.bot.wait_for("message", check=check)
                else:
                    print("Success!!")
                    break
            else:
                await ctx.send("You need to mention someone to continue!")
                message = await self.bot.wait_for("message", check=check)

def setup(bot):
    bot.add_cog(Games(bot))