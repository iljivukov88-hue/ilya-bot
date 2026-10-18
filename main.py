import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8695930213:AAEvOgS1RfTNaOPL9o6WHxJdz3QSESR4uoU"
LINK = "https://po6.cabinet-pocketoption.com/register/?lid=1176232&subId2=BABLO"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("📈 ПОЛУЧИТЬ СИГНАЛ", callback_data="sig"))
    kb.add(InlineKeyboardButton("💰 ЗАБРАТЬ БАБЛО", url=LINK))
    bot.send_message(m.chat.id, "🔥 Бот Ильи подключен!\nЖми сигнал:", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    p = random.choice(["EUR/USD OTC","GBP/USD OTC","USD/JPY OTC","BTC/USD OTC"])
    s = random.choice(["ВВЕРХ 🟢 2 МИН","ВНИЗ 🔴 2 МИН"])
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("🔄 ЕЩЕ СИГНАЛ", callback_data="sig"))
    kb.add(InlineKeyboardButton("💰 ЗАБРАТЬ БАБЛО", url=LINK))
    bot.edit_message_text(f"📊 {p}\n➡️ {s}", c.message.chat.id, c.message.message_id, reply_markup=kb)

bot.infinity_polling()
