# phonkd_bot - Builtin methods
<details>
  <summary><h5>phonkd_bot.call_on_message(message: Callable[[phonkd_bot.message], str])</h5></summary>
  <br>
  
  Tells the framework what function to call when it receives a message. The framework will pass a [discord message object](https://discordpy.readthedocs.io/en/stable/api.html#discord.Message) when it invokes the function. 
</details>

### Responding to messages
- Adding the `phonkd_bot.message` type hint to the `message` parameter allows your code editor to autocomplete attributes of the discord [`Message`](https://discordpy.readthedocs.io/en/stable/api.html#discord.Message) object, see their [documentation](https://discordpy.readthedocs.io/en/stable/api.html#discord.Message) for more information.
- The function passed into `call_on_message` will be called when a the bot receives a message. The return value is what the bot will respond with.
- The framework will pass a discord.Message object as a paramater to the function provided to `call_on_message`.
```python
def on_message(message: phonkd_bot.message):
    return "Hello!"

phonkd_bot.call_on_message(on_message)
```

### Activating the bot

```python
phonkd_bot.start()
```

### Logging Information

The `DiscordBot` class has a sub class called `logger`. The `logger` class has multiple methods that will help you debug or catch errors in your script. These methods are:
- `logger.info`
- `logger.warning`
- `logger.error`
- `logger.critical`

Here is an example script.

```python
import phonkd_bot

phonkd_bot.logger.info("info message")
phonkd_bot.logger.warning("warning message")
phonkd_bot.logger.error("error message")
phonkd_bot.logger.critical("critical error message")
```

This is the result.

![image of terminal containing logged information](https://i.imgur.com/wiIKZEQ.png)

### Example Discord Bot Script

```python
import phonkd_bot

def on_message(message: phonkd_bot.message):
    return "Hello!"

phonkd_bot.call_on_message(on_message)
phonkd_bot.start()
```

This is the result.

![image of discord bot saying hello](https://i.imgur.com/4hcMWHE.png)