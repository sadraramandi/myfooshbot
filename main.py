import telebot
import random

# توکن ربات تلگرام رو اینجا بزار
TOKEN = "8049027104:AAFVJAZexvEpCjXcke0lzqk3UgFnLMeTNYc"

bot = telebot.TeleBot(TOKEN)

# لیست جملات تصادفی
responses = [
    "کم زر بزن",
    "گوه نخور",
    "اسکل",
    "میدونستی خیلی احمقی؟",
    "جوون بچه خوشگل",
    "کم تر زر بزنی کسی نمیگه لالی",
    "چرا تو نمیمیری؟. برو زیر تریلی دیگه",
    "یه سول دارم چند تا درخت توته؟"
]

# هندل پیام‌های جدید در گروه
@bot.message_handler(func=lambda message: True)
def send_random_message(message):
    if message.chat.type in ["group", "supergroup"]:
        response = random.choice(responses)
        bot.reply_to(message, response)

print("🤖 ربات فعال شد...")
bot.infinity_polling()
