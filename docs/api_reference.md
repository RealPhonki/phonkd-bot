# phonkd_bot - Builtin methods
<details>
  <summary><h5>phonkd_bot.call_on_message(message: Callable[[phonkd_bot.message], str])</h5></summary>

  Tells the framework what function to call when it receives a message. The framework will pass a [discord message object](https://discordpy.readthedocs.io/en/stable/api.html#discord.Message) when it invokes the function. 
  
</details>
<details>
  <summary><h5>phonkd_bot.start()</h5></summary>

  Tells the framework to connect to the server, this method takes no parameters.
</details>

<details>
  <summary><h5>phonkd_bot.logger</h5></summary>

  phonkd_bot has a `logger` attribute with a few internal methods that will help you with debugging your script. These methods are:
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

</details>

<details>
  <summary><h5>Example bot script</h5></summary>

  ```python
  import phonkd_bot

  def on_message(message: phonkd_bot.message):
      return "Hello!"

  phonkd_bot.call_on_message(on_message)
  phonkd_bot.start()
  ```

  This is the result.

  ![image of discord bot saying hello](https://i.imgur.com/4hcMWHE.png)

</details>