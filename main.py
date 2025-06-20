import telebot
from config import token
<<<<<<< HEAD
from logic import Pokemon, Wizard, Fighter
from random import randint

bot = telebot.TeleBot(token)\

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
=======
from logic import Pokemon

bot = telebot.TeleBot(token)
>>>>>>> dad0949daf1e3887a7b6b22400ac611b60d699a3

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
<<<<<<< HEAD
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
=======
        pokemon = Pokemon(message.from_user.username)
>>>>>>> dad0949daf1e3887a7b6b22400ac611b60d699a3
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "🚫 Ты уже создал себе покемона")

<<<<<<< HEAD
@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            your_pok = Pokemon.pokemons[message.from_user.username]
            res = your_pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "🚫 Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "🚫 Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

=======
>>>>>>> dad0949daf1e3887a7b6b22400ac611b60d699a3
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

<<<<<<< HEAD
=======
# Реакция на любые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, " Извини, если тебе не понятно, загляни в список командв нижнем-левом углу.")

>>>>>>> dad0949daf1e3887a7b6b22400ac611b60d699a3
# Секретная команда
@bot.message_handler(commands=['ilikechocolatesomuchandilikesecretcommandsbecauseitiscool'])
def secret(message):
    bot.send_message(message.chat.id, "TypeError: This command is not allowed yet, but Chocolate is useful for you.")

<<<<<<< HEAD
# Реакция на любые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "💤 Извини, если тебе не понятно, загляни в список команд в нижнем-левом углу.")

bot.infinity_polling(none_stop=True)
=======
bot.infinity_polling(none_stop=True)
>>>>>>> dad0949daf1e3887a7b6b22400ac611b60d699a3
