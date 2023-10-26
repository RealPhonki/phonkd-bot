<div align="center">
<pre>
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗██╗  ██╗██████╗     ██████╗  ██████╗ ████████╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██║ ██╔╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██║   ██║██╔██╗ ██║█████╔╝ ██║  ██║    ██████╔╝██║   ██║   ██║   
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔═██╗ ██║  ██║    ██╔══██╗██║   ██║   ██║   
██║     ██║  ██║╚██████╔╝██║ ╚████║██║  ██╗██████╔╝    ██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
---------------------------------------------------------------
A discord bot framework that makes discord bot programming suprisingly easy
</pre>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## Installation

Not completed

## Creating a Discord Bot
1. Go to discord.com/developers/applications
2. Click `New Application`
3. Give the bot a name, agree to the terms, then click `Create`
4. (optional) give the bot a profile picture, tags, and or a description, then click `Save Changes`
5. Go to the `Bot` page on the side panel
6. (optional) give the bot a username
7. Click `Reset Token`, `Yes, do it!` and `Copy`, save the token somewhere safe
8. Allow `Presence Intent`, `Server Members Intent`, and `Message Content Intent`
9. Click `Save Changes`
10. Expand `OAuth2` on the side panel and go to `URL Generator`
11. Check `bot`, this will reveal `Bot Permissions`, you will need to check `Administrator` in this new section
12. Scroll down, and open the generated url in another tab
13. Select the server to add the bot to and click `Continue`
14. Make sure `Administrator` is checked and click `Authorize`
15. Do the captcha (if one appears) and close the window once you see `"Success!"` on your screen

## Dependencies
Create a file named `config.json` in the same directory as your main file. You will need to put your bot token (from discord.com/developers/applications) into the file.

```json
{
    "prefix": "/",
    "token": "YOUR BOT OKEN HERE"
}
```

## Usage Example

### Importing the bot

You will need to put this at the top of your code to access the framework.

```python
import phonkd_bot
```

### Creating a bot instance

You will need to create an instance of the `DiscordBot` class to make a discord bot.

```python
bot = phonkd_bot.DiscordBot()
```

### Responding to messages
- Adding the `phonkd_bot.message` type hint to the `message` parameter allows your code editor to autocomplete attributes of the discord `Message` object.
- Passing a function into the `call_on_message` method tells the framework where to get a response when a message is received.
- The framework will pass a discord.Message object as a paramater to the function provided to `call_on_Message`.
```python
def on_message(message: phonkd_bot.message):
    return "Hello!"

bot.call_on_message(on_message)
```

### Activating the bot

This should go at the bottom of your code.

```python
bot.start()
```

### Logging Information

The `DiscordBot` class has a sub class called `logger`. The `logger` class has multiple methods that will help you debug or catch errors in your script. These methods are:
- `logger.debug`
- `logger.info`
- `logger.warning`
- `logger.error`
- `logger.critical`

Here is an example script.

```python
bot.logger.debug("debug message")
bot.logger.info("info message")
bot.logger.warning("warning message")
bot.logger.error("error message")
bot.logger.critical("critical error message")
```

This is the result.

![[]](https://i.imgur.com/wiIKZEQ.png)

### Example Discord Bot Script

```python
import phonkd_bot

bot = phonkd_bot.DiscordBot()

def on_message(message: phonkd_bot.message):
    return "Hello!"

bot.call_on_message(on_message)
bot.start()
```

This is the result.

![Example Image](https://i.imgur.com/4hcMWHE.png)

## Meta
Gmail - phonkibusiness@gmail.com

Github - https://github.com/RealPhonki

Find me on the Python Discord Server - https://discord.com/invite/python

Discord Tag - `Phonki#0090`

Code distributed under the MIT license. See `LICENSE` for more information.