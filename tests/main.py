import phonkd_bot as bot

def on_message(message: bot.message):
    print(message.not_an_attribute)
    return "Hello!"

bot.call_on_message(on_message)
bot.start()