from framework.framework import api_handler

def on_message():
    pass

api_handler.call_on_message(on_message)
api_handler.activate_bot()