import telebot
from telebot import types

TOKEN = '8595383354:AAHk8IT4vmzdy9ofEiZbNcAGzQIjMt-AX5A'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("☕ ካፌዎች (Cafes)")
    btn2 = types.KeyboardButton("🍔 ሬስቶራንቶች (Restaurants)")
    btn3 = types.KeyboardButton("🌳 ፓርኮችና መዝናኛዎች")
    btn4 = types.KeyboardButton("ℹ️ ስለ ቦቱ")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, "እንኳን ወደ Addis Spot Finder ቦት በደህና መጡ! 👋\n\nእባክዎ መጎብኘት የሚፈልጉትን የቦታ አይነት ይምረጡ፦", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "☕ ካፌዎች (Cafes)":
        bot.reply_to(message, "📍 በአዲስ አበባ ያሉ ምርጥ ካፌዎች ዝርዝር በቅርቡ እዚህ ይጫናል...")
    elif message.text == "🍔 ሬስቶራንቶች (Restaurants)":
        bot.reply_to(message, "📍 ተወዳጅ የሬስቶራንቶች ዝርዝር በቅርቡ እዚህ ይጫናል...")
    elif message.text == "🌳 ፓርኮችና መዝናኛዎች":
        bot.reply_to(message, "📍 ለመዝናናት የሚሆኑ ምርጥ ፓርኮች በቅርቡ እዚህ ይጫናል...")
    elif message.text == "ℹ️ ስለ ቦቱ":
        bot.reply_to(message, "📱 ይህ ቦት በአዲስ አበባ ያሉ ምርጥ መዝናኛ ቦታዎችን በቀላሉ ለመጠቆም የተሰራ ነው።")

print("ቦቱ ስራ ጀምሯል...")
bot.infinity_polling()
