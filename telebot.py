import requests
import telebot

# Telegram bot token
TOKEN = '6473719227:AAFBCIuXLcAveb_6uEDWVI5cQWABBXjEDsU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['tc']) 
def get_tc_info(message):
    chat_id = message.chat.id
    received_tc = message.text.split(' ')[1]
    response = requests.get(f'https://rezidans.co/api/tc/api.php?tc={received_tc}')
    tc_info = response.text

    # Splitting the response into lines and sending each line as a separate message
    for line in tc_info.split('\n'):
        bot.send_message(chat_id, line)

bot.polling()

