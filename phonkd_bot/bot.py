# external imports
import discord
from discord.ext import commands
import importlib
import asyncio
import inspect
import json
import sys
import os

# local imports
from phonkd_bot.logger import logger

class DiscordAPIHandler():
    def __init__(self) -> None:
        # aliases
        self.CALLER_FILE = self.get_caller_file()
        self.CALLER_DIRECTORY = self.get_caller_directory(self.CALLER_FILE)

        # attributes
        self.config = self.load_config_file(self.CALLER_DIRECTORY)
        self.client = self.load_client()

        # initialize
        asyncio.run(self.main())

    """ Initializer methods """
    def get_caller_file(self):
        fname = inspect.currentframe()
        while fname.f_back:
            fname = fname.f_back
        caller_file = fname.f_globals['__file__']
        return caller_file

    def get_caller_directory(self, caller_file: str):
        caller_directory = os.path.dirname(os.path.abspath(caller_file))
        return caller_directory

    def load_config_file(self, directory: str) -> dict:
        config_path = directory + "/config.json"
        if not os.path.isfile(config_path):
            with open(config_path, 'w') as config:
                sys.exit("Config file not found")
        else:
            with open(config_path) as file:
                return json.load(file)

    def load_client(self) -> commands.Bot:
        # create a discord bot client and return it
        client = commands.Bot(command_prefix=commands.when_mentioned_or(self.config["prefix"]), intents=discord.Intents.all())
        client.logger = logger()
        client.callables = {"on_message": self.get_caller_function('on_message')}
        return client

    async def load(self) -> None:
        # get the path of hte current file
        path = os.path.realpath(f"{os.path.dirname(__file__)}/cogs")

        # if the cogs directory does not exist then cancel the script
        if not os.path.isdir(path):
            sys.exit('"cogs" directory does not exist')

        # loop through every filename in the cogs directory
        for filename in os.listdir(path):
            # only handle python files
            if filename.endswith(".py"):
                extension = filename[:-3]
                try:
                    # load the cog and log the information
                    await self.client.load_extension(f"phonkd_bot.cogs.{extension}")
                    self.client.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    # print the exception if there is one
                    exception = f"{type(e).__name__}: {e}"
                    self.client.logger.error(f"Failed to load extension {extension}\n{exception}")

    def get_caller_function(self, function_name: str):
        try:
            caller_module = importlib.import_module(self.CALLER_FILE)
            function = getattr(caller_module, function_name)
            return function
        except (ImportError, AttributeError):
            return None


    async def main(self) -> None:
        async with self.client:
            await self.load()
            await self.client.start(self.config["token"])