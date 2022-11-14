import asyncio
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from pytz import timezone
from pyairtable import Table
import discord
from discord.ext import commands
from discord import app_commands

AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_TRACKER_BASE_ID')
tz = timezone('US/Central')

class PlotTracker(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @app_commands.command(name='matplot_test', description='im testing again lol')
  async def button_test(self, interaction: discord.Interaction, x_axis_label: str, y_axis_label: str, title: str, line_label: str):
    table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, 'lol')
    xkcd_matplot(x_axis_label, y_axis_label, title, table, line_label)
    plot_file = discord.File(fp='./cogs/plots/xkcd_plot.png')
    await interaction.response.send_message(file=plot_file)

  @app_commands.command(name='track', description='Create a new record!')
  async def new_record(self, interaction: discord.Interaction, count: int, context: str) -> None:
    '''/new_record [quote] [context] - saves new record into Airtable'''
    table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, 'lol')

    timestamp=datetime.now(tz)
    success = await upload_to_airtable(table, [count, context])
    if success:
      await interaction.response.send_message('Record successfully saved to Airtable!', ephemeral=False)
    else:
      await interaction.response.send_message('Record failed to save to Airtable!', ephemeral=True)

def xkcd_matplot(x_axis_label, y_axis_label, title, table, line_label):
  table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, 'lol')
  records = pd.DataFrame(table.all(sort=['created']))
  count_list = [record['count'] for record in records['fields']]
  print(count_list)
  day_list = range(1, len(count_list) + 1)
  
  with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    line_f, = ax.plot(day_list, count_list, color = 'red', marker = 'o', markersize = 4, 
    markerfacecolor = 'red', label = line_label)
    # line_s, = 

    plt.title(title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)

    plt.legend(handles = [line_f])
    plt.savefig('./cogs/plots/xkcd_plot.png')

async def upload_to_airtable(airtable, fields):
  '''creates a record out of the fields, attempts to append record into airtable, returns a boolean'''
  try:
    table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, 'lol')
    airtable_df = pd.DataFrame(table.all())
    # airtable_col_names = list(airtable_df['fields'][0].keys())
    # record_dict = dict(zip(airtable_col_names, fields))
    airtable.create({
      'count': fields[0],
      'context': fields[1]
    })
    return True
  except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    return False

async def setup(bot: commands.Bot):
  '''adds cog to bot'''
  await bot.add_cog(PlotTracker(bot))