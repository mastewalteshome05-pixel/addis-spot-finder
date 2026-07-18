import telebot
from telebot import types
import requests

TOKEN = '8595383354:AAHk8IT4vmzdy9ofEiZbNcAGzQIjMt-AX5A'
bot = telebot.TeleBot(TOKEN)

# የ JSON መረጃው የሚገኝበት ድረ-ገጽ ሊንክ (Endpoint)
DATA_URL = "https://api.jsonbin.io/v3/b/YOUR_BIN_ID_HERE" 

def get_places_from_json(category):
    try:
        # ከ JSON endpoint መረጃውን መሳብ
        response = requests.get(DATA_URL)
        data = response.json()
        
        # የ JSON መዋቅርህን መሠረት በማድረግ መረጃውን መለየት
        # ምሳሌ፦ {"cafes": [{"name": "Tomoca", "location": "Piassa"}]}
        places = data.get("record", {}).get(category, [])
        
        if not places:
            return "❌ በአሁኑ ሰዓት ምንም የተመዘገበ ቦታ አልተገኘም።"
            
        text = f"📍 **የ{category} ዝርዝር፦**\n\n"
        for index, place in enumerate(places, 1):
            text += f"{index}. **{place['name']}**\n"
            text += f"   📍 አድራሻ፦ {place['location']}\n"
            text += f"   ✨ መግለጫ፦ {place['description']}\n\n"
        return text
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return "❌ መረጃውን ከሰርቨር ላይ ማምጣት አልተቻለም። እባክዎ ቆይተው ይሞክሩ።"

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "☕ ካፌዎች (Cafes)":
        # 'cafes' የሚለውን ቁልፍ በመላክ ከJSON እንዲፈልግ ማድረግ
        response_text = get_places_from_json("cafes")
        bot.reply_to(message, response_text, parse_mode="Markdown")
        
    elif message.text == "🍔 ሬስቶራንቶች (Restaurants)":
        response_text = get_places_from_json("restaurants")
        bot.reply_to(message, response_text, parse_mode="Markdown")

bot.infinity_polling()
