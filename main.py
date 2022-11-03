import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

class ChadowBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            description=f"Hi! I'm a bot that spits out a random quote from your favorite quote from the Sonic Fandubs by SnapCube!",
            intents=intents,
            application_id = os.environ.get('DISCORD_BOT_APP_ID')
        )
    async def load_extensions(self) -> None:
        '''loads the collection of commands in the cogs folder'''
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

    async def setup_hook(self) -> None:
        '''creates a webhook'''
        self.remove_command('help') # removes help command
        await self.load_extensions()
        await bot.tree.sync()

load_dotenv() # reads in the API tokens from .env

bot = ChadowBot()

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))