# import stuff
import phonkd_bot

bot = phonkd_bot.DiscordBot()

bot.logger.debug("debug message")
bot.logger.info("info message")
bot.logger.warning("warning message")
bot.logger.error("error message")
bot.logger.critical("critical error message")

def on_message(message: phonkd_bot.message):
    return "Hello"

bot.call_on_message(on_message)
bot.start()