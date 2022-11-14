import random
import asyncio
import discord
from discord.ext import commands
from discord import app_commands

class Morbius(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @app_commands.command(name='morbius', description="Remember when [um] and then proceeded to [uh] all over everyone? [ah] times.")
  async def morbius(self, interaction: discord.Interaction, um: str, uh: str, ah: str) -> None:
    await prompt_wait(interaction.channel)
    await interaction.response.send_message(f'Remember when {um} and then proceeded to {uh} all over everyone?', ephemeral=False)
    await prompt_wait(interaction.channel)
    await interaction.channel.send(f'{ah} times.')

async def prompt_wait(channel):
  '''shows lifelike typing in specified channel'''
  async with channel.typing():
    type_time = random.uniform(2, 3)
    await asyncio.sleep(type_time)

async def setup(bot: commands.Bot):
    await bot.add_cog(Morbius(bot))
