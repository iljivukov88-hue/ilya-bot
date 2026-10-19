import telebot, random, os, threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask

TOKEN = "8695930213:AAEvOgS1RfTnAOPL9o6WHxJdz"
LINK = "https://po6.cabinet-pocketoption.com"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("📈 ПОЛУЧИТЬ СИГНАЛ", callback_data="get"))
    kb.add(InlineKeyboardButton("💰 ЗАБРАТЬ БОНУС", url=LINK))
    bot.send_message(m.chat.id, "🔥 Бот Ильи\nЖми кнопку ниже 👇", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    p = random.choice(["EUR/USD OTC", "USD/JPY OTC"])
    d = random.choice(["ВВЕРХ 🟢 2 МИН", "ВНИЗ 🔴 2 МИН"])
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("🔄 Новый сигнал", callback_data="get"))
    kb.add(InlineKeyboardButton("PocketOption", url=LINK))
    bot.edit_message_text(f"🎯 {p}\n{d}", c.message.chat.id, c.message.message_id, reply_markup=kb)
    bot.answer_callback_query(c.id)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_web, daemon=True).start()
bot.infinity_polling()
