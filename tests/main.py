import phonkd_bot as bot

def on_message(message: bot.message):
    return "Hello!"

bot.call_on_message(on_message)
bot.start()