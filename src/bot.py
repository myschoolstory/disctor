import discord
from discord.ext import commands
import asyncio
from config import DISCORD_TOKEN, COMMAND_PREFIX
from torrent_client import download_torrent, upload_torrent, seed_torrent

# Set up the bot with a command prefix
bot = commands.Bot(command_prefix=COMMAND_PREFIX)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command(name='download')
async def download(ctx, torrent_url: str):
    """Command to download a torrent."""
    try:
        await ctx.send(f'Starting download for {torrent_url}...')
        result = download_torrent(torrent_url)
        await ctx.send(f'Download completed: {result}')
    except Exception as e:
        await ctx.send(f'Error downloading torrent: {e}')

@bot.command(name='upload')
async def upload(ctx, file_path: str):
    """Command to upload a torrent."""
    try:
        await ctx.send(f'Starting upload for {file_path}...')
        result = upload_torrent(file_path)
        await ctx.send(f'Upload completed: {result}')
    except Exception as e:
        await ctx.send(f'Error uploading torrent: {e}')

@bot.command(name='seed')
async def seed(ctx, torrent_url: str):
    """Command to seed a torrent."""
    try:
        await ctx.send(f'Starting seeding for {torrent_url}...')
        result = seed_torrent(torrent_url)
        await ctx.send(f'Seeding started: {result}')
    except Exception as e:
        await ctx.send(f'Error seeding torrent: {e}')

# Run the bot
bot.run(DISCORD_TOKEN)
