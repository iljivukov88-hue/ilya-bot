import telebot, random, os, threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask

TOKEN = "8695930213:AAEvOgS1RfTNaOPL9o6WHxJdz7"
LINK = "https://po6.cabinet-pocketoption.com/register/?lid=1176232&subId2=BABLO"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("📈 ПОЛУЧИТЬ СИГНАЛ", callback_data="sig"))
    kb.add(InlineKeyboardButton("💰 ЗАБРАТЬ БОНУС 100%", url=LINK))
    bot.send_message(m.chat.id, "🔥 Бот Ильи готов! Жми кнопку:", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    p = random.choice(["EUR/USD OTC","USD/JPY OTC","GBP/USD OTC"])
    d = random.choice(["ВВЕРХ 🟢 2 МИН","ВНИЗ 🔴 2 МИН"])
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("🔄 НОВЫЙ СИГНАЛ", callback_data="sig"))
    kb.add(InlineKeyboardButton("💰 БАБЛО - БОНУС", url=LINK))
    bot.edit_message_text(f"🔥 {p}\n{d}", c.message.chat.id, c.message.message_id, reply_markup=kb)
    bot.answer_callback_query(c.id)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_web, daemon=True).start()
bot.infinity_polling()
