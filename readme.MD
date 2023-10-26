<div align="center">
<pre>
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗██╗  ██╗██████╗     ██████╗  ██████╗ ████████╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██║ ██╔╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██║   ██║██╔██╗ ██║█████╔╝ ██║  ██║    ██████╔╝██║   ██║   ██║   
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔═██╗ ██║  ██║    ██╔══██╗██║   ██║   ██║   
██║     ██║  ██║╚██████╔╝██║ ╚████║██║  ██╗██████╔╝    ██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
---------------------------------------------------------------
A discord bot framework that makes discord bots easy
</pre>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## Installation

Not completed

## Creating a Discord Bot
1. Go to discord.com/developer/applications
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
Create a file named `config.json` in the same directory as your main file. The contents of the file should look like this.
```json
{
    "prefix": "/",
    "token": "YOUR TOKEN HERE"
}
```

## Usage Example

### Importing the bot
```python
import phonkd_bot
```

### Creating a bot instance
```python
phonkd_bot.DiscordBot()
```

### Responding to messages
- Adding the `phonkd_bot.message` type hint to the `message` parameter allows your code editor to autocomplete attributes of the discord `Message` object.
- Passing a function into the `call_on_message` method tells the framework where to get a response when a message is received.
- The framework will pass the discord.Message object as a paramater to the function provided to it.
```python
def on_message(message: phonkd_bot.message):
    return "Hello!"

bot.call_on_message(on_message)
```

### Running the bot
```python
bot.start()
```

### Example Script

```python
import phonkd_bot

bot = phonkd_bot.DiscordBot()

def on_message(message: phonkd_bot.message):
    return "Hello!"

bot.call_on_message(on_message)
bot.start()
```

This is the resulting bot.
![](hello_example.png)

## Meta
Phonki - phonkibusiness@gmail.com

Github Profile - https://github.com/RealPhonki

Discord Tag - `Phonki#0090`

Distributed under the MIT license. See `LICENSE` for more information.

## Contributing

Please don't contribute, I don't have time to review code changes