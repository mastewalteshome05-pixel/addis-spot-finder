import telebot
from telebot import types
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# ሬንደር እንዳይዘጋ የዌብ ሰርቨር መክፈቻ
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Starting server on port {port}")
    server.serve_forever()

# ሰርቨሩን ከጀርባ ማስነሳት
threading.Thread(target=run_server, daemon=True).start()

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
        cafes_text = (
            "☕ **በአዲስ አበባ ያሉ ምርጥ ካፌዎች ዝርዝር፦**\n\n"
            "1. **ቶሞካ ካፌ (Tomoca Coffee)**\n"
            "   📍 አድራሻ፦ ፒያሳ (ዋናው መሥሪያ ቤት) እና ቦሌ\n"
            "   ✨ መግለጫ፦ በኢትዮጵያ አንጋፋውና ምርጥ የተቆላ ቡና የሚያቀርብ ታዋቂ ካፌ。\n\n"
            "2. **ማክያቶ ካፌ (Macchiato Cafe)**\n"
            "   📍 አድራሻ፦ ቦሌ (ከኤድናሞል አጠገብ)\n"
            "   ✨ መግለጫ፦ ለስራ፣ ለንባብ እና ከጓደኞች ጋር ለመጨዋወት ምቹ ድባብ ያለው ካፌ。\n\n"
            "3. **ጋለሪ ካፌ (Gallery Cafe)**\n"
            "   📍 አድራሻ፦ ሣር ቤት\n"
            "   ✨ መግለጫ፦ ውብ የአትክልት ስፍራ እና ጸጥታ የሰፈነበት ድንቅ ቦታ。"
        )
        bot.reply_to(message, cafes_text, parse_mode="Markdown")
        
    elif message.text == "🍔 ሬስቶራንቶች (Restaurants)":
        restaurants_text = (
            "🍔 **ተወዳጅ የሬስቶራንቶች ዝርዝር፦**\n\n"
            "1. **ባህላዊ ምግብ አዳራሽ (Yod Abyssinia)**\n"
            "   📍 አድራሻ፦ ቦሌ ማተሚያ ቤት አካባቢ\n"
            "   ✨ መግለጫ፦ ምርጥ የሀገር ባህል ምግቦች ከደማቅ ባህላዊ እስክስታና ሙዚቃ ጋር。\n\n"
            "2. **ቅመም ሬስቶራንት (Kimen Restaurant)**\n"
            "   📍 አድራሻ፦ አትላስ\n"
            "   ✨ መግለጫ፦ ጣፋጭ የሀገር ውስጥና የውጭ ሀገር ምግቦችን በፅዱ ሁኔታ የሚያቀርብ。\n\n"
            "3. **ሮማ በርገር (Roma Burger)**\n"
            "   📍 አድራሻ፦ ሜክሲኮ እና ቪኤምሲ\n"
            "   ✨ መግለጫ፦ ፈጣን እና እጅግ ተወዳጅ የሆኑ በርገሮችን የሚያገኙበት ቦታ。"
        )
        bot.reply_to(message, restaurants_text, parse_mode="Markdown")
        
    elif message.text == "🌳 ፓርኮችና መዝናኛዎች":
        parks_text = (
            "🌳 **ለመዝናናት የሚሆኑ ምርጥ ፓርኮች፦**\n\n"
            "1. **አንድነት ፓርክ (Unity Park)**\n"
            "   📍 አድራሻ፦ ታላቁ ቤተ-መንግሥት (ፒያሳ አካባቢ)\n"
            "   ✨ መግለጫ፦ ታሪካዊ ህንፃዎች፣ የእንስሳት ማቆያ እና ውብ መናፈሻ የያዘ ታላቅ ፓርክ。\n\n"
            "2. **ወዳጅነት ፓርክ (Friendship Park)**\n"
            "   📍 አድራሻ፦ ፍልውሃ (ከአራት ኪሎ ዝቅ ብሎ)\n"
            "   ✨ መግለጫ፦ ሰው ሰራሽ ሀይቅ፣ የውሃ እሽክርክሪት (Fountain) እና የእግር ጉዞ መስመር ያለው。\n\n"
            "3. **እንጦጦ ፓርክ (Entoto Park)**\n"
            "   📍 አድራሻ፦ እንጦጦ ተራራ ላይ\n"
            "   ✨ መግለጫ፦ በጫካ ውስጥ የተሰራ፣ ለስፖርት፣ ለሳይክል እና ንፁህ አየር ለመቀበል ፍፁም ምርጥ ቦታ。"
        )
        bot.reply_to(message, parks_text, parse_mode="Markdown")
        
    elif message.text == "ℹ️ ስለ ቦቱ":
        bot.reply_to(message, "📱 ይህ ቦት በአዲስ አበባ ያሉ ምርጥ መዝናኛ ቦታዎችን፣ ካፌዎችን እና ሬስቶራንቶችን በቀላሉ ለመጠቆም የተሰራ ነው።")

print("ቦቱ ስራ ጀምሯል...")
bot.infinity_polling()
