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
        guild = member.guild
        system_channel = guild.system_channel
        if system_channel is not None:
            await system_channel.send(f"Welcome to {guild.name} {member.name}!")
        else:
            print("There isn't a system messages channel set.")

    #When a member leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        system_channel = guild.system_channel
        if system_channel is not None:
            await system_channel.send(f"{guild.name} will miss you {member.name}!")
        else:
            print("There isn't a system messages channel set.")

def setup(bot):
    bot.add_cog(Events(bot))
