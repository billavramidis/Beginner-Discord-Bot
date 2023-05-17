from disnake.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name = "connect", 
        description = "Connects to a voice channel.",
        category = "Music"
    )
    async def connect(ctx):
        voice_state = ctx.author.voice
        if not voice_state:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        voice_channel = voice_state.channel
        if ctx.guild.voice_client and ctx.guild.voice_client.is_connected():
            if ctx.guild.voice_client.channel == voice_channel:
                await ctx.send("The bot is already in this voice channel.")
            else:
                await ctx.guild.voice_client.move_to(voice_channel)
                await ctx.send(f"Moved to {voice_channel}.")
        else:
            await voice_channel.connect()
            await ctx.send(f"Connected to {voice_channel}.")

    @commands.slash_command(
        name = "disconnect", 
        description = "Disconnects from a voice channel.",
        category = "Music"
    )
    async def disconnect(ctx):
        voice_client = ctx.guild.voice_client
        if voice_client:
            await voice_client.disconnect()
            await ctx.send("Successfully disconnected from the voice channel.")
        else:
            await ctx.send("The bot is not connected to a voice channel.")
    
def setup(bot):
    bot.add_cog(Music(bot))