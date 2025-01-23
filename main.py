import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve token from .env file
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Debugging
if not TOKEN:
    print("Error: Token is missing. Ensure the DISCORD_BOT_TOKEN variable is set in your .env file.")
    exit(1)  # Exit if token is missing

# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="hello", description="Replies with Hello, World!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, World!")

@bot.tree.command(name="goodnight", description="Have sweet dreams!")
async def goodnight(interaction: discord.Interaction):
    await interaction.response.send_message("GOOD NIGHT! HAVE LOTS OF SWEET DREAMS AND SLEEP TIGHT! BEEP BOOP!")

# Run the bot
bot.run(TOKEN)
