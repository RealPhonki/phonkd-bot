import phonkd_bot

bot = phonkd_bot.DiscordBot()

def on_message(message: phonkd_bot.message):
    return "Hello!"

bot.call_on_message(on_message)
bot.start()