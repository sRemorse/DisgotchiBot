import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="ping")
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping", colour=discord.Colour.blue())
        embed.add_field(name=f"{self.bot.user.name}'s Latency (ms): ", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo")
    async def server_info(self, ctx):
        embed = discord.Embed(title="Server Information", colour=discord.Colour.blue())
        embed.add_field(name="Server name", value=f"{ctx.guild.name}", inline=True)
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=True)
        embed.add_field(name="Owner", value=f"{ctx.guild.owner}", inline=True)
        embed.add_field(name="User count", value=f"{ctx.guild.member_count}", inline=True)
        embed.add_field(name="Text channel count", value=f"{len(ctx.guild.channels)}", inline=True)
        embed.add_field(name="Voice channel count", value=f"{len(ctx.guild.voice_channels)}", inline=True)
        embed.add_field(name="Emojis", value=f"{len(ctx.guild.emojis)}", inline=True)
        embed.add_field(name="Stickers", value=f"{len(ctx.guild.stickers)}", inline=True)
        embed.add_field(name="Roles", value=f"{len(ctx.guild.roles)}", inline=True)
        embed.add_field(name="", value=f"", inline=False)
        embed.add_field(name="Created at", value=f"{ctx.guild.created_at}", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        embed.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))