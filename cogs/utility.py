import datetime
import time

import discord
from discord.ext import commands
import discord.app_commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="Display the bots current latency (ms).")
    @discord.app_commands.checks.cooldown(rate=1, per=10)
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)

        colour = (
            discord.Colour.green() if latency < 100 else
            discord.Colour.yellow() if latency < 200 else
            discord.Colour.red()
        )

        embed = discord.Embed(description=f"{latency}ms", colour=colour)
        await interaction.response.send_message(embed=embed)

    @discord.app_commands.command(name="serverinfo", description="Provide information on the current server.")
    @discord.app_commands.checks.cooldown(rate=1, per=10)
    async def server_info(self, interaction: discord.Interaction):
        created_at = interaction.guild.created_at
        formatted_time = created_at.astimezone(datetime.timezone.utc).strftime("%B %d, %Y at %I:%M %p UTC")
        embed = discord.Embed(title="Server Information", colour=discord.Colour.green())
        embed.add_field(name="Server name", value=f"{interaction.guild.name}", inline=True)
        embed.add_field(name="Server ID", value=f"{interaction.guild.id}", inline=True)
        embed.add_field(name="Owner", value=f"{interaction.guild.owner}", inline=True)
        embed.add_field(name="User count", value=f"{interaction.guild.member_count}", inline=True)
        embed.add_field(name="Text channel count", value=f"{len(interaction.guild.channels)}", inline=True)
        embed.add_field(name="Voice channel count", value=f"{len(interaction.guild.voice_channels)}", inline=True)
        embed.add_field(name="Roles", value=f"{len(interaction.guild.roles)}", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="Created at", value=f"{formatted_time}", inline=True)
        embed.set_thumbnail(url=interaction.guild.icon)
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        print("Initialising uptime timer")
        startTime = time.time()

    @discord.app_commands.command(name="uptime", description="Display the bots current uptime.")
    @discord.app_commands.checks.cooldown(rate=1, per=10)
    async def uptime(self, interaction: discord.Interaction):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        embed = discord.Embed(description=f"{self.bot.user.name} has been running for `{uptime}`",
                              colour=discord.Colour.green())
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
