"""
This class acts as the front end to the user. I seperated it from the main class to prevent the user
from seeing internal methods that may be confusing
"""

# external imports
from collections.abc import Callable
from discord import Message as message
from inspect import signature
from asyncio import run

# local import
from .api_handler import DiscordAPIHandler

api_handler = DiscordAPIHandler()
logger = api_handler.LOGGER

def start() -> None:
    """
    Starts the bot client and loads dependencies.
    """
    run(api_handler.main())

def call_on_message(function: Callable[[message], str]) -> None:
    """
    The bot will call the parameter passed into this method whenever it receives a message
    """

    # check if the object passed is a function
    if not callable(function):
        api_handler.LOGGER.error(f"Failed to load function '{function}'")
        return
    
    # check if the function only has 1 parameter
    parameters = signature(function).parameters
    if len(parameters) != 1:
        api_handler.LOGGER.error(f"Invalid number of parameters in {function}, please only specify one.")
        return
    
    api_handler.client.callables["on_message"] = function