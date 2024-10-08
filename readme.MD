<div align="center">
<pre>
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗██╗  ██╗██████╗     ██████╗  ██████╗ ████████╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██║ ██╔╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██║   ██║██╔██╗ ██║█████╔╝ ██║  ██║    ██████╔╝██║   ██║   ██║   
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔═██╗ ██║  ██║    ██╔══██╗██║   ██║   ██║   
██║     ██║  ██║╚██████╔╝██║ ╚████║██║  ██╗██████╔╝    ██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
---------------------------------------------------------------------------------
</pre>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

# WARNING, THIS REPOSITORY IS NO LONGER MAINTAINED

Phonkd_bot is a free discord bot framework made with the intent to help beginner programmers learn python. It allows you to take console-based programs and convert them into discord bots by substituting the `input` and `print` functions. It takes the [Discord library](https://discordpy.readthedocs.io/en/stable/api.html) and abstracts all of the complex functionality to make writing these programs simpler.

## Setup

#### Installation

Before installing phonkd_bot, you must check that Python is installed on your machine. To find out, open a command prompt (if you have Windows) or a terminal (if you have MacOS or Linux) and type this:

```sh
python --version
```

If a message such as "`Python 3.8.10`" appears, it means that Python is correctly installed. If an error message appears, it means that it is not installed yet. You must then go to the [official website](https://www.python.org/) and install it.

Once Python is installed, you have to perform a final check: you have to see if pip is installed. Generally, pip is pre-installed with Python but we are never sure. Same as for Python, type the following command:

```sh
pip --version
```

If a message such as "`pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)`" appears, you are ready to install the library. To install it, enter this command:

```sh
pip install phonkd_bot
```

#### Creating a Discord Bot
Now you will need to create a discord bot, to do so, follow these instructions:
1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
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

#### Setting up the environment

Create a file named `config.json` in the same directory as your script. Copy and paste your bot token (from [discord.com/developers](https://discord.com/developers/applications)) into the file, it should look something like this:

```json
{
    "token": "MTE2nze0MDYzmzk5MTk5MTMxNg.Gm0Mnf.kmsdIjbvOZFMIs94ipxOCt70aLs3lKQsl0VaPE"
}
```
*This token is not real, you will need to replace it with your own.*

## Help
If you want to use this framework check out the reference documentation on the [docs page](https://github.com/RealPhonki/phonkd-bot/blob/main/docs/api_reference.md). If you find issues with this library please reach out to me.

## Meta
Gmail - phonkibusiness@gmail.com

Github - https://github.com/RealPhonki

Find me on the Python Discord Server - https://discord.com/invite/python

Discord Tags - `realphonki`

Code distributed under the MIT license. See `LICENSE` for more information.
