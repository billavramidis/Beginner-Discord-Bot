from disnake.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

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
    bot.add_cog(TicTacToe(bot))