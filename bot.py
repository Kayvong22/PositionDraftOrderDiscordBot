import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from .env
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def shuffle(ctx, *, names: str):
    """Shuffles a list of names given as input"""

    # print(f"Raw input:\n{names}")  # Print input to console (for debugging)
    
    name_list = [name.strip() for name in names.split("\n") if name.strip()]  # Ensure correct splitting
    # print(f"Parsed list: {name_list}")  # Print parsed list to console

    random.shuffle(name_list)  # Shuffle names
    shuffled_names = "\n".join(name_list)
    # print(f"Shuffled list: {shuffled_names}")  # Rejoin as a string
    await ctx.send(f"Here is the position draft order:\n```\n{shuffled_names}\n```")

bot.run(TOKEN)
