import disnake
import os
from disnake.ext import commands

from tokens import disc_token

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '/', intents = intents)

# The following code loads every extension.
cog_tree = filter(lambda dir: not "__pycache__" in dir[0], os.walk("cogs"))

for cog_branch in cog_tree:
    dir = cog_branch[0]
    bot.load_extensions(dir)
    
bot.run(disc_token) 