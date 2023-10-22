# external imports
import discord
from discord.ext import commands
import asyncio
import json
import sys
import os

# local imports
from framework.bot_logger import logger

class DiscordAPIHandler():
    def __init__(self) -> None:
        # attributes
        self.config = self.load_config()
        self.client = self.load_client()

    """ Initializer methods """
    def load_config(self) -> dict:
        # check if config.json exists
        if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
            sys.exit('"config.json" file not found')
        # open and return the contents
        else:
            with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
                return json.load(file)

    def load_client(self) -> commands.Bot:
        # create a discord bot client and return it
        client = commands.Bot(command_prefix=commands.when_mentioned_or(self.config["prefix"]), intents=discord.Intents.all())
        client.logger = logger()
        client.callables = {"on_message": None}
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
                    await self.client.load_extension(f"framework.cogs.{extension}")
                    self.client.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    # print the exception if there is one
                    exception = f"{type(e).__name__}: {e}"
                    self.client.logger.error(f"Failed to load extension {extension}\n{exception}")

    async def main(self) -> None:
        async with self.client:
            await self.load()
            await self.client.start(self.config["token"])

    """ Framework methods """
    def call_on_message(self, function: callable) -> None:
        """
        Calls on your function whenever a message is recieved and passes in a "message" object.
        To find out about the propeerties of message objects you can visit this link:
        https://discordpy.readthedocs.io/en/latest/api.html#message
        """
        self.client.callables["on_message"] = function

    def activate_bot(self) -> None:
        """
        Activates the bot
        """
        asyncio.run(self.main())

api_handler = DiscordAPIHandler()