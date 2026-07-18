import os
import threading
import telebot
from telebot import types
from flask import Flask

# Render የዌብሳይት ፖርት (Port) እንዲያገኝ የሚያደርግ ቀላል የፍላስክ ሰርቨር ማዋቀር
app = Flask('')

@app.route('/')
def home():
    return "Bot is running perfectly!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ፍላስክን በስተጀርባ (Background Thread) ማስነሳት
threading.Thread(target=run_flask).start()

# የቴሌግራም ቦት መለያ (Token)
TOKEN = '8595383354:AAHk8IT4vmzdy9ofEiZbNcAGzQIjMt-AX5A'
bot = telebot.TeleBot(TOKEN)

# የቦታ ጥቆማዎች በቀጥታ ላንተ እንዲመጡ ያንተ የቴሌግራም ID
ADMIN_ID = "657483920" 

# የቦታዎች መረጃ (ዳታቤዝ)
PLACES_DATA = {
    "cafes": [
        {
            "name": "ቶሞካ ካፌ (Tomoca Coffee)",
            "area": "ፒያሳ",
            "address": "📍 አድራሻ፦ ፒያሳ (ዋናው መሥሪያ ቤት)",
            "desc": "✨ መግለጫ፦ በኢትዮጵያ አንጋፋውና ምርጥ የተቆላ ቡና የሚያቀርብ ታዋቂ ካፌ።",
            "map_url": "https://maps.google.com/?q=Tomoca+Coffee+Piassa",
            "photo": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb"
        },
        {
            "name": "ማክያቶ ካፌ (Macchiato Cafe)",
            "area": "ቦሌ",
            "address": "📍 አድራሻ፦ ቦሌ (ከኤድናሞል አጠገብ)",
            "desc": "✨ መግለጫ፦ ለስራ፣ ለንባብ እና ከጓደኞች ጋር ለመጨዋወት ምቹ ድባብ ያለው ካፌ።",
            "map_url": "https://maps.google.com/?q=Bole+Edna+Mall",
            "photo": "https://images.unsplash.com/photo-1498804103079-a6351b050096"
        }
    ],
    "restaurants": [
        {
            "name": "ዮድ አቢሲኒያ (Yod Abyssinia)",
            "area": "ቦሌ",
            "address": "📍 አድራሻ፦ ቦሌ ማተሚያ ቤት አካባቢ",
            "desc": "✨ መግለጫ፦ ምርጥ የሀገር ባህል ምግቦች ከደማቅ ባህላዊ እስክስታና ሙዚቃ ጋር።",
            "map_url": "https://maps.google.com/?q=Yod+Abyssinia+Addis+Ababa",
            "photo": "https://images.unsplash.com/photo-1533777857889-4be7c70b33f7"
        },
        {
            "name": "ሮማ በርገር (Roma Burger)",
            "area": "ሜክሲኮ",
            "address": "📍 አድራሻ፦ ሜክሲኮ አካባቢ",
            "desc": "✨ መግለጫ፦ ፈጣን እና እጅግ ተወዳጅ የሆኑ በርገሮችን የሚያገኙበት ቦታ።",
            "map_url": "https://maps.google.com/?q=Mexico+Addis+Ababa",
            "photo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
        }
    ],
    "parks": [
        {
            "name": "አንድነት ፓርክ (Unity Park)",
            "area": "ፒያሳ",
            "address": "📍 አድራሻ፦ ታላቁ ቤተ-መንግሥት",
            "desc": "✨ መግለጫ፦ ታሪካዊ ህንፃዎች፣ የእንስሳት ማቆያ እና ውብ መናፈሻ የያዘ ታላቅ ፓርክ።",
            "map_url": "https://maps.google.com/?q=Unity+Park+Addis+Ababa",
            "photo": "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
        }
    ]
}

user_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_states[message.chat.id] = None
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("☕ ካፌዎች (Cafes)")
    btn2 = types.KeyboardButton("🍔 ሬስቶራንቶች (Restaurants)")
    btn3 = types.KeyboardButton("🌳 ፓርኮችና መዝናኛዎች")
    btn4 = types.KeyboardButton("✍️ ቦታ ጠቁም (Suggest)")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(
        message.chat.id, 
        "እንኳን ወደ Addis Spot Finder በደህና መጡ! 👋\n\n"
        "🔍 **ለመፈለግ**፦ የአካባቢውን ስም ቀጥታ ይጻፉልኝ (ምሳሌ፦ ቦሌ ወይም ፒያሳ)\n\n"
        "እባክዎ ከታች ካሉት አማራጮች አንዱን ይምረጡ፦", 
        reply_markup=markup
    )

def send_places_by_category(chat_id, category_key):
    places = PLACES_DATA.get(category_key, [])
    for place in places:
        caption = f"🌟 **{place['name']}**\n\n{place['address']}\n{place['desc']}"
        
        inline_markup = types.InlineKeyboardMarkup()
        map_btn = types.InlineKeyboardButton("📍 በካርታው ላይ እይ (Google Maps)", url=place['map_url'])
        inline_markup.add(map_btn)
        
        try:
            bot.send_photo(chat_id, place['photo'], caption=caption, reply_markup=inline_markup, parse_mode="Markdown")
        except:
            bot.send_message(chat_id, caption, reply_markup=inline_markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_id = message.chat.id
    text = message.text

    if user_states.get(chat_id) == "waiting_for_suggestion":
        user_states[chat_id] = None
        bot.reply_to(message, "🙏 ስለ ጥቆማዎ እናመሰግናለን! መረጃውን ፈትሸን ወደ ሲስተሙ የምናስገባው ይሆናል።")
        
        admin_text = f"📩 **አዲስ የቦታ ጥቆማ ደርሷል!**\n\n👤 ከተጠቃሚ፦ @{message.from_user.username or 'የለውም'}\n📝 ዝርዝር፦ {text}"
        try:
            bot.send_message(ADMIN_ID, admin_text)
        except:
            pass
        return

    if text == "☕ ካፌዎች (Cafes)":
        send_places_by_category(chat_id, "cafes")
    elif text == "🍔 ሬስቶራንቶች (Restaurants)":
        send_places_by_category(chat_id, "restaurants")
    elif text == "🌳 ፓርኮችና መዝናኛዎች":
        send_places_by_category(chat_id, "parks")
    elif text == "✍️ ቦታ ጠቁም (Suggest)":
        user_states[chat_id] = "waiting_for_suggestion"
        bot.reply_to(message, "📝 እባክዎ የቦታውን ስም፣ አድራሻ እና መግለጫ በአንድ መልዕክት ላይ ጽፈው ይላኩናል።")
    else:
        found = False
        search_query = text.lower()
        
        for category, places in PLACES_DATA.items():
            for place in places:
                if search_query in place['name'].lower() or search_query in place['area'].lower():
                    caption = f"🔍 **የፍለጋ ውጤት፦**\n\n🌟 **{place['name']}**\n\n{place['address']}\n{place['desc']}"
                    inline_markup = types.InlineKeyboardMarkup()
                    map_btn = types.InlineKeyboardButton("📍 በካርታው ላይ እይ (Google Maps)", url=place['map_url'])
                    inline_markup.add(map_btn)
                    
                    try:
                        bot.send_photo(chat_id, place['photo'], caption=caption, reply_markup=inline_markup, parse_mode="Markdown")
                    except:
                        bot.send_message(chat_id, caption, reply_markup=inline_markup, parse_mode="Markdown")
                    found = True
                    
        if not found:
            bot.reply_to(message, f"🔍 ይቅርታ፣ ከ '{text}' ጋር የሚገናኝ ቦታ በአሁኑ ሰዓት ማግኘት አልቻልኩም። እባክዎ በሌላ ቃል ይሞክሩ (ለምሳሌ፦ ቦሌ፣ ፒያሳ)።")

print("Advanced ቦት ከሰርቨር ድጋፍ ጋር ስራ ጀምሯል...")
bot.infinity_polling()
