import phonkd_bot as bot

def on_message(message: bot.message, invalid_num_params: bool):
    return "Hello!"

bot.call_on_message(on_message)
bot.start()