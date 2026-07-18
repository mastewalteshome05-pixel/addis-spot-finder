import os
import threading
import telebot
from telebot import types
from flask import Flask

# Render የዌብሳይት ፖርት (Port) እንዲያገኝ የሚያደርግ ቀላል የፍላስክ ሰርቨር ማዋቀር
app = Flask('')

@app.route('/')
def home():
    return "Bot is running perfectly with 12 Languages, Smart Search & Global Data!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ፍላስክን በስተጀርባ (Background Thread) ማስነሳት
threading.Thread(target=run_flask).start()

# የቴሌግራም ቦት መለያ (Token)
TOKEN = '8595383354:AAHk8IT4vmzdy9ofEiZbNcAGzQIjMt-AX5A'
bot = telebot.TeleBot(TOKEN)

# የቦታ ጥቆማዎች እና የተጠቃሚ መረጃዎች በቀጥታ ላንተ እንዲመጡ ያንተ የቴሌግራም ID
ADMIN_ID = "657483920" 

# የብዙ ቋንቋዎች መዝገበ-ቃላት (12 Languages)
STRINGS = {
    "am": {"welcome": "እንኳን ወደ Addis Spot Finder በደህና መጡ! 👋\n🔍 **ለመፈለግ**፦ የአካባቢውን ወይም የቦታውን ስም ቀጥታ ይጻፉልኝ (ምሳሌ፦ ቦሌ፣ አሜሪካ)\n\nእባክዎ ከታች ካሉት አማራጮች አንዱን ይምረጡ፦", "btn_cafes": "☕ ካፌዎች", "btn_restaurants": "🍔 ሬስቶራንቶች", "btn_parks": "🌳 ፓርኮች", "btn_suggest": "✍️ ቦታ ጠቁም", "suggest_prompt": "📝 እባክዎ የቦታውን ስም፣ አድራሻ እና መግለጫ ይጻፉ።\n\n💡 **ማሳሰቢያ በፎቶ**፦ የቦታው ውብ ፎቶ እንዲታይ ከፈለጉ፣ ከGoogle Maps ወይም Google Image ላይ የፎቶውን ሊንክ (URL) አብረው ያያይዙልን።", "suggest_thanks": "🙏 ለጥቆማው እናመሰግናለን! መረጃውን ፈትሸን ወደ ሲስተሙ የምናስገባው ይሆናል።", "not_found": "🔍 ይቅርታ፣ ያሰገቡትን ቦታ ማግኘት አልቻልኩም። እባክዎ በሌላ ቃል ይሞክሩ።", "map_btn": "📍 በካርታው ላይ እይ", "search_res": "🔍 የፍለጋ ውጤት፦"},
    "en": {"welcome": "Welcome to Addis Spot Finder! 👋\n🔍 **To Search**: Directly type the name of the place or country (e.g., Bole, America)\n\nPlease choose an option below:", "btn_cafes": "☕ Cafes", "btn_restaurants": "🍔 Restaurants", "btn_parks": "🌳 Parks", "btn_suggest": "✍️ Suggest a Place", "suggest_prompt": "📝 Please write the name, address, and description of the place.\n\n💡 **Photo Note**: To display a nice photo, please copy and paste a photo link (URL) from Google Maps or Google Images.", "suggest_thanks": "🙏 Thank you for your suggestion! We will review and add it soon.", "not_found": "🔍 Sorry, no places found matching your search. Please try another word.", "map_btn": "📍 View on Map", "search_res": "🔍 Search Result:"},
    "om": {"welcome": "Baga gara Addis Spot Finder nagaan dhuftan! 👋\n🔍 **Barbaaduuf**: Maqaa naannoo ykn biyyaa qajeeltoon barreessaa (Fkn: Bole, America)\n\nMee filannoowwan gadii keessaa tokko filadha:", "btn_cafes": "☕ Kafeewwan", "btn_restaurants": "🍔 Bakkoota Nyaataa", "btn_parks": "🌳 Paarkota", "btn_suggest": "✍️ Bakka Eeri", "suggest_prompt": "📝 Maaloo maqaa bakkichaa, teessoo fi ibsa isaa barreessaa.\n\n💡 **Hubannoo Fakkii**: Fakkii bareedaan akka argamuuf, Google Maps ykn Google Image irraa liankii fakkii (URL) kophisanii asitti nuu ergaa.", "suggest_thanks": "🙏 Eeruu keessaniif galatoomaa! Nuti sakatta'ree sirna keessa ni galchina.", "not_found": "🔍 Bakkichaan walitti kan hidhatu argachuu hin dandeenye. Maaloo jecha biraatiin yaalaa.", "map_btn": "📍 Kaartaa irratti ilaali", "search_res": "🔍 Bua'aa Barbaachaa:"},
    "ti": {"welcome": "እንቋዕ ናብ Addis Spot Finder ብደሓን መጻእኹም! 👋\n🔍 ንምድላይ ሽም እቲ ቦታ ወይ ዓዲ ጽሓፉ።", "btn_cafes": "☕ ካፌታት", "btn_restaurants": "🍔 እንዳ መግቢ", "btn_parks": "🌳 ፓርክታት", "btn_suggest": "✍️ ሓሳብ ሃብ", "suggest_prompt": "📝 በጃኹም ሽም እቲ ቦታን ኣድራሻን ጽሓፉ። (ካብ Google ፎቶ ሊንክ እንተሃሊዩ ይውስኹ)", "suggest_thanks": "🙏 የቀንየልና! መረዳእታ መርሚርና ናብ ሲስተም ከነእትዎ ኢና።", "not_found": "🔍 ይቕረታ፣ እቲ ዝደለኹምዎ ቦታ ኣይተረኽበን።", "map_btn": "📍 ኣብ ካርታ ርኣይ", "search_res": "🔍 ውጽኢት ምስትንታን፦"},
    "so": {"welcome": "Ku soo dhawaada Addis Spot Finder! 👋\n🔍 Ku qor magaca meesha ama dalka aad raadinayso.", "btn_cafes": "☕ Kafeeyaal", "btn_restaurants": "🍔 Maqaayado", "btn_parks": "🌳 Beeraha", "btn_suggest": "✍️ Meel Talo Bixi", "suggest_prompt": "📝 Fadlan qor magaca iyo ciwaanka meesha. (Haddii aad sawir ka haysato Google ku dar linkiga)", "suggest_thanks": "🙏 Waad ku mahadsan tay taladaada! Waan dib u eegi doonaa.", "not_found": "🔍 Waan ka xunnahay, meesha lama helin.", "map_btn": "📍 Ka eeg Khariidadda", "search_res": "🔍 Natiijada Raadinta:"},
    "ar": {"welcome": "مرحبًا بك في Addis Spot Finder! 👋\n🔍 اكتب اسم المكان أو الدولة للبحث عنه (مثال: بولي، أمريكا).", "btn_cafes": "☕ مقاهي", "btn_restaurants": "🍔 مطاعم", "btn_parks": "🌳 حدائق", "btn_suggest": "✍️ اقترح مكانًا", "suggest_prompt": "📝 يرجى كتابة اسم المكان وعنوانه ووصفه مع رابط الصورة إن وجد.", "suggest_thanks": "🙏 شكرًا لاقتراحك! سنقوم بمراجعته وإضافته قريبًا.", "not_found": "🔍 عذرًا، لم يتم العثور على المكان.", "map_btn": "📍 عرض على الخريطة", "search_res": "🔍 نتيجة البحث:"},
    "fr": {"welcome": "Bienvenue sur Addis Spot Finder ! 👋\n🔍 Tapez le nom du lieu ou du pays pour rechercher.", "btn_cafes": "☕ Cafés", "btn_restaurants": "🍔 Restaurants", "btn_parks": "🌳 Parcs", "btn_suggest": "✍️ Suggérer un lieu", "suggest_prompt": "📝 Veuillez écrire le nom, l'adresse et ajouter un lien photo de Google.", "suggest_thanks": "🙏 Merci pour votre suggestion !", "not_found": "🔍 Désolé, lieu non trouvé.", "map_btn": "📍 Voir sur la carte", "search_res": "🔍 Résultat de la recherche:"},
    "es": {"welcome": "¡Bienvenido a Addis Spot Finder! 👋\n🔍 Escribe el nombre del lugar o país para buscar.", "btn_cafes": "☕ Cafés", "btn_restaurants": "🍔 Restaurantes", "btn_parks": "🌳 Parques", "btn_suggest": "✍️ Sugerir un lugar", "suggest_prompt": "📝 Por favor escriba el nombre, dirección y enlace de imagen de Google.", "suggest_thanks": "🙏 ¡Gracias por tu sugerencia!", "not_found": "🔍 Lo siento, lugar no encontrado.", "map_btn": "📍 Ver en el mapa", "search_res": "🔍 Resultado de búsqueda:"},
    "de": {"welcome": "Willkommen bei Addis Spot Finder! 👋\n🔍 Geben Sie den Namen des Ortes oder Landes ein.", "btn_cafes": "☕ Cafés", "btn_restaurants": "🍔 Restaurants", "btn_parks": "🌳 Parks", "btn_suggest": "✍️ Ort vorschlagen", "suggest_prompt": "📝 Bitte schreiben Sie Name, Adresse und Google-Bildlink auf.", "suggest_thanks": "🙏 Vielen Dank für Ihren Vorschlag!", "not_found": "🔍 Entschuldigung, Ort nicht gefunden.", "map_btn": "📍 Auf Karte anzeigen", "search_res": "🔍 Suchergebnis:"},
    "it": {"welcome": "Benvenuto su Addis Spot Finder! 👋\n🔍 Digita il nome del luogo o del paese da cercare.", "btn_cafes": "☕ Caffè", "btn_restaurants": "🍔 Ristoranti", "btn_parks": "🌳 Parchi", "btn_suggest": "✍️ Suggerisci un luogo", "suggest_prompt": "📝 Si preга di scrivere il nome, l'indirizzo e il link della foto.", "suggest_thanks": "🙏 Grazie per il tuo suggerimento!", "not_found": "🔍 Spiacenti, luogo non trovato.", "map_btn": "📍 Mappa", "search_res": "🔍 Risultato della ricerca:"},
    "ru": {"welcome": "Добро пожаловать в Addis Spot Finder! 👋\n🔍 Введите название места или страны для поиска.", "btn_cafes": "☕ Кафе", "btn_restaurants": "🍔 Рестораны", "btn_parks": "🌳 Парки", "btn_suggest": "✍️ Предложить место", "suggest_prompt": "📝 Пожалуйста, напишите название, адрес и ссылку на фото из Google.", "suggest_thanks": "🙏 Спасибо за ваше предложение!", "not_found": "🔍 Извините, место не найдено.", "map_btn": "📍 Показать на карте", "search_res": "🔍 Результат поиска:"},
    "zh": {"welcome": "欢迎来到 Addis Spot Finder！ 👋\n🔍 输入地点或国家名称进行搜索（例如：Bole、美国）。", "btn_cafes": "☕ 咖啡馆", "btn_restaurants": "🍔 餐厅", "btn_parks": "🌳 公园", "btn_suggest": "✍️ 推荐地点", "suggest_prompt": "📝 请写下地点的名称、地址和来自Google的图片链接。", "suggest_thanks": "🙏 感谢您的建议！我们会尽快审核并添加。", "not_found": "🔍 抱歉，未找到该地点。", "map_btn": "📍 在地图上查看", "search_res": "🔍 搜索结果："}
}

# ግሎባል የቦታዎች መረጃ ዳታቤዝ (የሀገር ስም እና Keywords ተጨምሮበታል)
PLACES_DATA = {
    "cafes": [
        {
            "name": "ቶሞካ ካፌ (Tomoca Coffee)", 
            "area": "ኢትዮጵያ ፒያሳ አዲስ አበባ ethiopia addis ababa piassa ☕", 
            "address": "📍 አድራሻ፦ ፒያሳ፣ አዲስ አበባ (ኢትዮጵያ)", 
            "desc": "✨ መግለጫ፦ በኢትዮጵያ አንጋፋውና ምርጥ የተቆላ ቡና የሚያቀርብ ታዋቂ ካፌ።", 
            "map_url": "https://maps.google.com/?q=Tomoca+Coffee+Piassa", 
            "photo": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb"
        },
        {
            "name": "ስታርባክስ ኒው ዮርክ (Starbucks New York)", 
            "area": "አሜሪካ ኒውዮርክ america usa new york manhattan hotel ☕", 
            "address": "📍 Address: Times Square, New York (USA)", 
            "desc": "✨ ታዋቂው የአሜሪካ የቡና መሸጫ በኒው ዮርክ ታይምስ ስኩዌር።", 
            "map_url": "https://maps.google.com/?q=Starbucks+Times+Square+New+York", 
            "photo": "https://images.unsplash.com/photo-1541167760496-1628856ab772"
        }
    ],
    "restaurants": [
        {
            "name": "ዮድ አቢሲኒያ (Yod Abyssinia)", 
            "area": "ኢትዮጵያ ቦሌ አዲስ አበባ ethiopia addis ababa bole 🍔", 
            "address": "📍 አድራሻ፦ ቦሌ ማተሚያ ቤት አካባቢ፣ አዲስ አበባ", 
            "desc": "✨ መግለጫ፦ ምርጥ የሀገር ባህል ምግቦች ከደማቅ ባህላዊ እስክስታና ሙዚቃ ጋር።", 
            "map_url": "https://maps.google.com/?q=Yod+Abyssinia+Addis+Ababa", 
            "photo": "https://images.unsplash.com/photo-1533777857889-4be7c70b33f7"
        },
        {
            "name": "ማክዶናልድ ዋሽንግተን (McDonald's Washington)", 
            "area": "አሜሪካ ዋሽንግተን america usa washington dc burger hotel 🍔", 
            "address": "📍 Address: Downtown, Washington D.C. (USA)", 
            "desc": "✨ ፈጣንና ተወዳጅ የሆኑ በርгеሮችን የሚያገኙበት የአሜሪካ መመгеቢያ።", 
            "map_url": "https://maps.google.com/?q=McDonalds+Washington+DC", 
            "photo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
        }
    ],
    "parks": [
        {
            "name": "አንድነት ፓርክ (Unity Park)", 
            "area": "ኢትዮጵያ ፒያሳ አዲስ አበባ ethiopia addis ababa piassa 🌳", 
            "address": "📍 አድራሻ፦ ታላቁ ቤተ-መንግሥት፣ አዲስ አበባ", 
            "desc": "✨ መግለጫ፦ ታሪካዊ ህንፃዎች፣ የእንስሳት ማቆያ እና ውብ መናፈሻ የያዘ ታላቅ ፓርክ።", 
            "map_url": "https://maps.google.com/?q=Unity+Park+Addis+Ababa", 
            "photo": "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
        },
        {
            "name": "ሴንትራል ፓርክ (Central Park New York)", 
            "area": "አሜሪካ ኒውዮርክ america usa new york central park 🌳", 
            "address": "📍 Address: Manhattan, New York City (USA)", 
            "desc": "✨ በአሜሪካ እጅግ ታዋቂውና ውቡ ግዙፍ የተፈጥሮ መዝናኛ ፓርк።", 
            "map_url": "https://maps.google.com/?q=Central+Park+New+York", 
            "photo": "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
        }
    ]
}

user_languages = {}
user_states = {}

@bot.message_handler(commands=['start'])
def choose_language(message):
    chat_id = message.chat.id
    user_states[chat_id] = None
    
    # ተጠቃሚው ቦቱን ሲጀምር ሙሉ መረጃውን ለአድሚን በምስጢር መላክ
    user_info = (
        f"👤 **አዲስ ተጠቃሚ ቦቱን ጀምሯል!**\n\n"
        f"📝 ስም: {message.from_user.first_name} {message.from_user.last_name or ''}\n"
        f"🆔 ID: `{chat_id}`\n"
        f"🔗 Username: @{message.from_user.username or 'የለውም'}"
    )
    try: bot.send_message(ADMIN_ID, user_info, parse_mode="Markdown")
    except: pass

    # የ 12 ቋንቋዎች Inline ማሳያ ቁልፎች (ባለ 2 ረድፍ አደራጃጀት)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("አማርኛ 🇪🇹", callback_data="lang_am"),
        types.InlineKeyboardButton("English 🇬🇧", callback_data="lang_en"),
        types.InlineKeyboardButton("Afaan Oromoo 🇪🇹", callback_data="lang_om"),
        types.InlineKeyboardButton("ትግርኛ 🇪🇹", callback_data="lang_ti"),
        types.InlineKeyboardButton("Soomaali 🇸🇴", callback_data="lang_so"),
        types.InlineKeyboardButton("العربية 🇸🇦", callback_data="lang_ar"),
        types.InlineKeyboardButton("Français 🇫🇷", callback_data="lang_fr"),
        types.InlineKeyboardButton("Español 🇪🇸", callback_data="lang_es"),
        types.InlineKeyboardButton("Deutsch 🇩🇪", callback_data="lang_de"),
        types.InlineKeyboardButton("Italiano 🇮🇹", callback_data="lang_it"),
        types.InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru"),
        types.InlineKeyboardButton("中文 🇨🇳", callback_data="lang_zh")
    )
    bot.send_message(chat_id, "🌐 Choose Your Language / ቋንቋ ይምረጡ፦", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def set_language(call):
    chat_id = call.message.chat.id
    lang_code = call.data.split("_")[1]
    user_languages[chat_id] = lang_code
    bot.delete_message(chat_id, call.message.message_id)
    send_main_menu(chat_id, lang_code)

def send_main_menu(chat_id, lang):
    ln = STRINGS[lang]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton(ln["btn_cafes"]), types.KeyboardButton(ln["btn_restaurants"]),
        types.KeyboardButton(ln["btn_parks"]), types.KeyboardButton(ln["btn_suggest"])
    )
    bot.send_message(chat_id, ln["welcome"], reply_markup=markup, parse_mode="Markdown")

def send_places_by_category(chat_id, category_key, lang):
    places = PLACES_DATA.get(category_key, [])
    ln = STRINGS[lang]
    for place in places:
        caption = f"🌟 **{place['name']}**\n\n{place['address']}\n{place['desc']}"
        inline_markup = types.InlineKeyboardMarkup()
        inline_markup.add(types.InlineKeyboardButton(ln["map_btn"] + " (Google Maps)", url=place['map_url']))
        try: bot.send_photo(chat_id, place['photo'], caption=caption, reply_markup=inline_markup, parse_mode="Markdown")
        except: bot.send_message(chat_id, caption, reply_markup=inline_markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_id = message.chat.id
    text = message.text
    lang = user_languages.get(chat_id, "am") # ካልመረጠ አማርኛ default ይሆናል
    ln = STRINGS[lang]

    # የቦታ ጥቆማዎችን ከአድራሻና ከGoogle ፎቶ መመሪያ ጋር ተቀብሎ ለአድሚን መላክ
    if user_states.get(chat_id) == "waiting_for_suggestion":
        user_states[chat_id] = None
        bot.reply_to(message, ln["suggest_thanks"])
        admin_text = (
            f"📩 **አዲስ የቦታ ጥቆማ ደርሷል!**\n\n"
            f"👤 ከተጠቃሚ፦ {message.from_user.first_name} (@{message.from_user.username or 'የለውም'})\n"
            f"🆔 ID: `{chat_id}`\n"
            f"📝 ዝርዝር መረጃ እና ሊንክ፦\n{text}"
        )
        try: bot.send_message(ADMIN_ID, admin_text)
        except: pass
        return

    # የቁልፎች ማረጋገጫ (ከሁሉም ቋንቋዎች ቁልፍ ጋር ይነፃፀራል)
    is_cafe = any(text == STRINGS[k]["btn_cafes"] for k in STRINGS)
    is_rest = any(text == STRINGS[k]["btn_restaurants"] for k in STRINGS)
    is_park = any(text == STRINGS[k]["btn_parks"] for k in STRINGS)
    is_sugg = any(text == STRINGS[k]["btn_suggest"] for k in STRINGS)

    if is_cafe: send_places_by_category(chat_id, "cafes", lang)
    elif is_rest: send_places_by_category(chat_id, "restaurants", lang)
    elif is_park: send_places_by_category(chat_id, "parks", lang)
    elif is_sugg:
        user_states[chat_id] = "waiting_for_suggestion"
        bot.reply_to(message, ln["suggest_prompt"])
    
    # 🔍 እጅግ የላቀ ግሎባል የጽሁፍ ፍለጋ ሲስተም (Global & Smart Text Search)
    else:
        found = False
        search_query = text.lower()
        for category, places in PLACES_DATA.items():
            for place in places:
                # በስም ወይም በሀገር/አካባቢ Keywords ውስጥ ካለ ይፈልጋል
                if search_query in place['name'].lower() or search_query in place['area'].lower():
                    caption = f"{ln['search_res']}\n\n🌟 **{place['name']}**\n\n{place['address']}\n{place['desc']}"
                    inline_markup = types.InlineKeyboardMarkup()
                    inline_markup.add(types.InlineKeyboardButton(ln["map_btn"] + " (Google Maps)", url=place['map_url']))
                    try: bot.send_photo(chat_id, place['photo'], caption=caption, reply_markup=inline_markup, parse_mode="Markdown")
                    except: bot.send_message(chat_id, caption, reply_markup=inline_markup, parse_mode="Markdown")
                    found = True
        if not found:
            bot.reply_to(message, ln["not_found"])

print("Advanced ግሎባል ቦት በ12 ቋንቋዎች ስራ ጀምሯል...")
bot.infinity_polling()
