import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name='ban', description='Ban a user who violates the rules')
@app_commands.describe(user='The user to ban', reason='The reason for the ban')
async def ban(interaction: discord.Interaction, user: discord.User, reason: str):
    try:
        await interaction.guild.ban(user, reason=reason)
        await interaction.response.send_message(f'Banned {user.mention} for {reason}')
    except Exception as e:
        await interaction.response.send_message(f'Failed to ban {user.mention}: {e}')

if __name__ == '__main__':
    bot.run(TOKEN)