import disnake
from disnake.ext import commands

from tokens import disc_token

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '/', intents = intents)

# Loads the events
bot.load_extension('events')

# Loads the miscellaneous commands
bot.load_extension('commands.misc')

# Loads the music commands
bot.load_extension('commands.music')
    
bot.run(disc_token)