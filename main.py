from datetime import datetime
import telebot
import time as t

bot = telebot.TeleBot("YOUR TOKEN")

@bot.message_handler(commands=["start"])
def start_comand(message):
    chat_id = message.chat.id
    now = datetime.now()
    date = now.strftime("%Y/%m/%d")
    time = now.strftime("%H.%M.%S")
    main_message = f"""
текущяя дата и время: 
год, месяц, день: {date}
час, минута, секунда: {time}"""
    bot.send_message(chat_id, main_message)

bot.infinity_polling()
