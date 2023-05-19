from disnake.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #When the bot starts
    @commands.Cog.listener()
    async def on_ready(self):
        print("The bot is ready for use!")

    #When a member joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1107384611690000516)
        await channel.send(f"Welcome to the server {member.name}!")

    #When a member leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1107384611690000516)
        await channel.send(f"We will miss you {member.name}!")

def setup(bot):
    bot.add_cog(Events(bot))
