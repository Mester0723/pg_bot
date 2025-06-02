import telebot
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привет, добро пожаловать в генератор покемонов!\n"
                                      "📃 Я бот для создания покемонов.\n"
                                      "👇 Напиши /go, чтобы создать покемона.")

# Обработчик команды /go или /start
@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "🚫 Ты уже создал себе покемона")

@bot.message_handler(commands=['ilikechocolatesomuchandilikesecretcommandsbecauseitiscool'])
def secret(message):
    bot.send_message(message.chat.id, "Слишком длинная команда, хватит тратить кучу времени на её написание, этого ведь ничего не даст!\n"
                                      "Ах! Беру свои слова обратно! Потому что любишь шоколад, кто его может не любить? Это же прекрастное дополнение для десертов!\n"
                                      "Секретные команды? Что за чужь! Тебе лишь бы занятся бесполезной чепухой!? Тьфу!!!")

bot.infinity_polling(none_stop=True)