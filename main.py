import discord
from discord import app_commands
from discord.ext import commands

import time
from cred import *

bot = commands.Bot(command_prefix=Prefix, intents=discord.Intents.all())
start_time = time.time()

@bot.event
async def on_ready():
    # Sync the slash commands with Discord
    await bot.tree.sync()
    print(f"✨| {Name} is Live")

@bot.tree.command(name="ping", description=f"Gets the ping for {Name}")
async def ping(interaction: discord.Interaction):
    latency = bot.latency * 1000
    await interaction.response.send_message(f"Pong! 🏓 `Latency: {latency:.2f} ms`")

@bot.tree.command(name="invite", description=f"Gets the invite for {Name}")
async def invite(interaction: discord.Interaction):
    button = discord.ui.Button(label="Add to Server", url=OAuth2)
    view = discord.ui.View()
    view.add_item(button)
    await interaction.response.send_message(view=view)

@bot.tree.command(name="uptime", description=f"Show uptime for {Name}")
async def uptime(interaction: discord.Interaction):
    current_time = time.time()
    uptime_seconds = int(current_time - start_time)

    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    await interaction.response.send_message(f"🕛| `Uptime: {hours}h {minutes}m {seconds}s`")

@bot.tree.command(name="help", description="Displays a list of all commands and their descriptions.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title=f"Help for {Name}", color=discord.Color.blue())
    
    embed.add_field(name="1. Ping", value=f"Gets the ping for {Name}\n- Usage: `/ping`", inline=False)
    embed.add_field(name="2. Invite", value=f"Gets the invite link for {Name}'s server\n- Usage: `/invite`", inline=False)
    embed.add_field(name="3. Uptime", value=f"Shows the bot's uptime\n- Usage: `/uptime`", inline=False)
    
    
    await interaction.response.send_message(embed=embed)

bot.run(Token)
