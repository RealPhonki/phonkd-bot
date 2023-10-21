# external imports
import discord
from discord.ext import commands
import platform
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
        self.callables = {}

    """ Initializer methods """

    def load_config(self) -> dict:
        if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
            sys.exit('"config.json" file not found')
        else:
            with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
                return json.load(file)

    def load_client(self) -> commands.Bot:
        client = commands.Bot(command_prefix=commands.when_mentioned_or(self.config["prefix"]), intents=discord.Intents.all())
        client.logger = logger()
        return client

    async def main(self) -> None:
        async with self.client:
            await self.client.start(self.config["token"])

    async def load(self) -> None:
        # for every python file in the cogs folder
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                extension = filename[:-3]
                try:
                    # load the python extension and print a cool message
                    await self.client.load_extension(f"cogs.{extension}")
                    self.client.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    # print the exception if there is one
                    exception = f"{type(e).__name__}: {e}"
                    self.client.logger.error(f"Failed to load extension {extension}\n{exception}")

    """ Framework methods """

    def call_on_message(self, function: callable) -> None:
        """
        Takes in a function that will be called whenever a message is received
        """
        self.callables["on_message"] = function

    def activate_bot(self) -> None:
        asyncio.run(self.main())

api_handler = DiscordAPIHandler()