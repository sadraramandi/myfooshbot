import telebot
import random

# توکن ربات تلگرام رو اینجا بزار
TOKEN = "8049027104:AAFVJazexvEpCjXcke0lzqk3UgFnLMeTNYc"

bot = telebot.TeleBot(TOKEN)

# لیست جملات برای همه کاربران
responses_general = [
    "کم زر بزن",
    "گوه نخور",
    "اسکل",
    "میدونستی خیلی احمقی؟",
    "جوون بچه خوشگل",
    "کم تر زر بزنی کسی نمیگه لالی",
    "چرا تو نمیمیری؟ برو زیر تریلی دیگه",
    "یه سوال دارم، چند تا درخت توته؟"
]

# لیست جملات مخصوص کاربر خاص
responses_sadra = ["چشم", "اوکی", "باشه, "ご主人様の目 (ごしゅじんさまのめ"]

# هندل پیام‌های جدید در گروه
@bot.message_handler(func=lambda message: True)
def send_random_message(message):
    if message.chat.type in ["group", "supergroup"]:
        if message.from_user.username == "sadradarziramandi":
            response = random.choice(responses_sadra)
        else:
            response = random.choice(responses_general)
        bot.reply_to(message, response)

print("🤖 ربات فعال شد...")
bot.infinity_polling()
