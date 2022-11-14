import asyncio
from venv import create
import discord
import os
from pytz import timezone
from pyairtable import Table
import random
from datetime import datetime
from discord.ext import commands
from discord import app_commands
import pandas as pd

tz = timezone('US/Eastern')

class RandomQuote(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @app_commands.command(name='quote', description='Generate a random quote!')
  async def quote(self, interaction: discord.Interaction) -> None:
    await prompt_wait(interaction.channel)
    await interaction.response.send_message('Quote created!', ephemeral=True)
    await interaction.channel.send(generate_quote())

  @app_commands.command(name='shadow_quote', description='Generate a random Shadow quote!')
  async def shadow_quote(self, interaction: discord.Interaction) -> None:
    await prompt_wait(interaction.channel)
    await interaction.response.send_message('Quote created!', ephemeral=True)
    await interaction.channel.send(generate_shadow_quote())

  @app_commands.command(name='specific_quote', description='Generate a random quote from a specific character!')
  async def quote(self, interaction: discord.Interaction) -> None:
    await prompt_wait(interaction.channel)
    await interaction.response.send_message('Quote created!', ephemeral=True)
    await interaction.channel.send(generate_quote())
    
async def prompt_wait(channel):
  '''shows lifelike typing in specified channel'''
  async with channel.typing():
    type_time = random.uniform(1, 1.5)
    await asyncio.sleep(type_time)

def generate_quote():
  df = pd.read_csv('cogs/Scripts/sonic_fandub_scripts.csv')
  quote_info = df.sample()
  name_quote = quote_info.iat[0,0]
  text_quote = quote_info.iat[0,1]
  return (f"{name_quote}: {text_quote}")

def generate_shadow_quote():
  df = pd.read_csv('cogs/Scripts/sonic_fandub_scripts.csv')
  shadow_quotes = df[df['name'] == 'Shadow']
  name_quote = shadow_quotes.iat[0,0]
  text_quote = shadow_quotes.iat[0,1]
  return (f"{name_quote}: {text_quote}")

async def setup(bot: commands.Bot):
  '''adds cog to bot'''
  await bot.add_cog(RandomQuote(bot))