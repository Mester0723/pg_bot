import telebot
from config import token
from logic import Pokemon, Wizard, Fighter
<<<<<<< HEAD
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = telebot.TeleBot(token)
=======
from random import randint

bot = telebot.TeleBot(token)\
>>>>>>> 5373d4a06ff51fc911156e2fa4141136964eb5c8

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))

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
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "🚫 Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
<<<<<<< HEAD
        attacker = message.from_user.username
        defender = message.reply_to_message.from_user.username
        if not attacker or not defender:
            bot.send_message(message.chat.id, "🚫 У обоих пользователей должен быть username в Telegram!")
            return
        if defender in Pokemon.pokemons and attacker in Pokemon.pokemons:
            enemy = Pokemon.pokemons[defender]
            your_pok = Pokemon.pokemons[attacker]
=======
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            your_pok = Pokemon.pokemons[message.from_user.username]
>>>>>>> 5373d4a06ff51fc911156e2fa4141136964eb5c8
            res = your_pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "🚫 Сражаться можно только с покемонами")
    else:
<<<<<<< HEAD
        bot.send_message(message.chat.id, "🚫 Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")
=======
            bot.send_message(message.chat.id, "🚫 Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")
>>>>>>> 5373d4a06ff51fc911156e2fa4141136964eb5c8

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
quiz_data = [
    {
        "question": "❓ Какой покемон является водным типом?",
        "options": ["Пикачу", "Сквиртл", "Чармандер", "Бульбазавр"],
        "correct": 1,
        "explanation": "Сквиртл — водный покемон."
    },
    {
        "question": "❓ Какой покемон эволюционирует в Charizard?",
        "options": ["Пикачу", "Сквиртл", "Чармандер", "Бульбазавр"],
        "correct": 2,
        "explanation": "Чармандер эволюционирует в Charizard."
    },
    {
        "question": "❓ Какой покемон известен как 'Пикачу'?",
        "options": ["Пикачу", "Сквиртл", "Чармандер", "Бульбазавр"],
        "correct": 0,
        "explanation": "Пикачу — это Пикачу!"
    },
    {
        "question": "❓ Какой покемон является легендарным?",
        "options": ["Мьюту", "Сквиртл", "Чармандер", "Бульбазавр"],
        "correct": 0,
        "explanation": "Мьюту — легендарный покемон."
    },
    {
        "question": "❓ Какой покемон может использовать 'Вспышку'?",
        "options": ["Пикачу", "Сквиртл", "Чармандер", "Бульбазавр"],
        "correct": 0,
        "explanation": "Пикачу может использовать 'Вспышку'."
    }
]

# Квиз с вопросами о покемонах
@bot.message_handler(commands=['quiz'])
def quiz(message):
    send_quiz_question(message.chat.id, 0)

def send_quiz_question(chat_id, q_num):
    if q_num < len(quiz_data):
        q = quiz_data[q_num]
        markup = InlineKeyboardMarkup()
        for idx, option in enumerate(q["options"]):
            markup.add(InlineKeyboardButton(option, callback_data=f"quiz_{q_num}_{idx}"))
        bot.send_message(chat_id, f"📃 Вопрос {q_num+1}/{len(quiz_data)}:\n{q['question']}", reply_markup=markup)
    else:
        bot.send_message(chat_id, "🎉 Квиз завершён! Спасибо за участие.")

# Обработчик ответов на вопросы квиза
@bot.callback_query_handler(func=lambda call: call.data.startswith("quiz_"))
def handle_quiz_answer(call):
    _, q_num, selected = call.data.split("_")
    q_num = int(q_num)
    selected = int(selected)
    correct = quiz_data[q_num]["correct"]

    # Удаляем сообщение с вопросом
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception:
        pass  # Если сообщение уже удалено или нет прав

    if selected == correct:
        bot.answer_callback_query(call.id, text="✅ Правильно!")
    else:
        bot.answer_callback_query(call.id, text="❌ Неправильно!")

    send_quiz_question(call.message.chat.id, q_num + 1)

=======
>>>>>>> 5373d4a06ff51fc911156e2fa4141136964eb5c8
# Секретная команда
@bot.message_handler(commands=['ilikechocolatesomuchandilikesecretcommandsbecauseitiscool'])
def secret(message):
    bot.send_message(message.chat.id, "TypeError: This command is not allowed yet, but Chocolate is useful for you.")

# Реакция на любые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "💤 Извини, если тебе не понятно, загляни в список команд в нижнем-левом углу.")

bot.infinity_polling(none_stop=True)