import telebot
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привет, добро пожаловать в генератор покемонов!\n"
                                      "📃 Я бот для создания покемонов.\n"
                                      "👇 Напиши /go, чтобы создать покемона.")

# Обработчик команды /go
@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "🚫 Ты уже создал себе покемона")

# Кормление покемона
@bot.message_handler(commands=['feed'])
def feed(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        result = pokemon.feed()
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "🚫 Сначала создай покемона с помощью команды /go")

# Достижения покемона
@bot.message_handler(commands=['achievements'])
def achievements(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        ach = pokemon.get_achievements()
        if ach:
            bot.send_message(message.chat.id, "🏆 Твои достижения:\n" + "\n".join(ach))
        else:
            bot.send_message(message.chat.id, "🔍 Пока нет достижений.\n"
                                              "🍔 Кормите и развивайте покемона!")
    else:
        bot.send_message(message.chat.id, "🚫 Сначала создай покемона с помощью команды /go")

# Уровень и опыт покемона
@bot.message_handler(commands=['level'])
def level(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        bot.send_message(
            message.chat.id,
            f"🔝 Уровень покемона {pokemon.name}: {pokemon.level}\n"
            f"➰ Опыт: {pokemon.exp}"
        )
    else:
        bot.send_message(message.chat.id, "🚫 Сначала создай покемона с помощью команды /go")

# Информация о покемоне
@bot.message_handler(commands=['info'])
def info(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        bot.send_message(message.chat.id, pokemon.info())
    else:
        bot.send_message(message.chat.id, "🚫 Сначала создай покемона с помощью команды /go")

# Реакция на любые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, " Извини, если тебе не понятно, загляни в список командв нижнем-левом углу.")

# Секретная команда
@bot.message_handler(commands=['ilikechocolatesomuchandilikesecretcommandsbecauseitiscool'])
def secret(message):
    bot.send_message(message.chat.id, "TypeError: This command is not allowed yet, but Chocolate is useful for you.")

bot.infinity_polling(none_stop=True)
