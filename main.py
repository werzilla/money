#money 
@bot.message_handler(func=lambda message: True)
def handler_message(message):
    bot.reply_to(message, message.text)
