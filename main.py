import asyncio
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("-------------------")
    print("The bot is ready!")
    print(f"Logged in as {bot.user} in {len(bot.guilds)} guilds")
    print(f"Status: {bot.status}")
    print(f"Activity: {bot.activity}")
    print("-------------------")


async def load_cogs() -> None:
    print("Loading extensions")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded: {filename}")

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    print("Cooldown error triggered")
    if isinstance(error, discord.app_commands.CommandOnCooldown):
        embed = discord.Embed(description=f"Please wait {int(error.retry_after)} seconds.", colour=discord.Colour.yellow())
        await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=error.retry_after)

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

load_dotenv()
asyncio.run(main())