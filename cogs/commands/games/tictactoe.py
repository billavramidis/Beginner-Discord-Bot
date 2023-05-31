from disnake.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name = "tictactoe",
        description = "You play Tic-Tac-Toe with someone."
    )
    async def tictactoe(self, ctx):
        
        channel = ctx.channel

        print(channel)
        
        def check_first(first):
            return first.author == ctx.author and first.channel == channel
        
        await ctx.send("Welcome to Tic-Tac-Toe! To play mention an other server member!")
        message = await self.bot.wait_for("message", check=check_first)
        
        while True:
            if message.mentions:
                first_player = ctx.user
                second_player = message.mentions[0]
                if first_player == second_player:
                    await ctx.send("You can't mention yourself! Mention someone else to continue or type 'exit' to exit!")
                    message = await self.bot.wait_for("message", check=check_first)
                else:
                    await ctx.send(f"{second_player.mention} do you want to play with {first_player.mention}?")
                    print("Success!!!!")
                    break
            elif message.content.lower() == 'exit':
                await ctx.send("You have successfully exited the game!")
                break
            else:
                await ctx.send("You need to mention someone to continue or type 'exit' to exit!")
                message = await self.bot.wait_for("message", check=check_first)

def setup(bot):
    bot.add_cog(TicTacToe(bot))