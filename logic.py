from random import randint
from datetime import datetime, timedelta
import requests

class Pokemon:
    # Словари для хранения покемонов и достижений
    pokemons = {}
    achievements = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer            

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(50, 150)
        self.attack_power = randint(20, 100)
        self.defense = randint(10, 80)
        self.type = self.get_type()
        self.abilities = self.get_abilities()
        self.level = 1
        self.power = randint(10, 50)
        self.exp = 0
        self.feed_count = 0
        self.last_feed_time = None
        Pokemon.achievements.setdefault(pokemon_trainer, [])

        Pokemon.pokemons[pokemon_trainer] = self
        

    def __init__(enemy, pokemon_trainer):

        enemy.pokemon_trainer = pokemon_trainer

        enemy.pokemon_number = randint(1,1000)
        enemy.img = enemy.get_img()
        enemy.name = enemy.get_name()
        enemy.hp = randint(50, 150)
        enemy.power = randint(10, 50)
        enemy.attack_power = randint(20, 100)
        enemy.defense = randint(10, 80)
        enemy.type = enemy.get_type()
        enemy.abilities = enemy.get_abilities()

        Pokemon.pokemons[pokemon_trainer] = enemy

    # Метод для кормления покемона
    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        if self.last_feed_time is None:
            self.hp = min(self.hp + hp_increase, 200)
            self.last_feed_time = current_time
            next_feed_time = self.last_feed_time + timedelta(seconds=feed_interval)
            return (
                f"🍔 Покемон покормлен впервые!\n"
                f"❤️ Текущее здоровье: {self.hp}\n"
                f"⏰ Следующее кормление возможно после: {next_feed_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp = min(self.hp + hp_increase, 200)
            self.last_feed_time = current_time
            next_feed_time = self.last_feed_time + delta_time
            return (
                f"💓 Здоровье покемона увеличено.\n"
                f"❤️ Текущее здоровье: {self.hp}\n"
                f"⏰ Следующее кормление возможно после: {next_feed_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        else:
            next_feed_time = self.last_feed_time + delta_time
            wait_seconds = int((next_feed_time - current_time).total_seconds())
            return (
                f"🚫 Рано кормить!\n"
                f"🍔 Следующее кормление через {wait_seconds} секунд.\n"
                f"⏰ Можно будет покормить после: {next_feed_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    # Метод для проверки повышения уровня
    def check_level_up(self):
        required_exp = self.level * 20
        while self.exp >= required_exp:
            self.exp -= required_exp
            self.level += 1
            self.attack += 5
            self.defense += 3
            self.hp = min(self.hp + 10, 200)
            required_exp = self.level * 20

    # Метод для проверки и выдачи достижений
    def check_achievements(self):
        ach = Pokemon.achievements[self.pokemon_trainer]
        if self.feed_count >= 10 and "Сытый покемон" not in ach:
            ach.append("Сытый покемон")
        if self.level >= 5 and "Пятый уровень!" not in ach:
            ach.append("Пятый уровень!")

    # Получить список достижений
    def get_achievements(self):
        return Pokemon.achievements[self.pokemon_trainer]

    # Метод для получения картинки покемона через API
    def get_img(self):
        img_url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(img_url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return f'https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png/revision/latest/scale-to-width-down/700?cb=20181021155144&path-prefix=ru'
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    # Метод для получения типа покемона через API
    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            types = data.get('types', [])
            if types:
                return types[0]['type']['name']
        return "normal"

    # Метод для получения способностей покемона через API
    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            abilities = data.get('abilities', [])
            return [a['ability']['name'] for a in abilities]
        return []
    
    # Метод для атаки покемона
    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"

    # Метод класса для получения информации
    def info(self):
        return (
            f"👾 Имя покемона: {self.name}\n"
            f"🔷 Тип: {self.type}\n"
            f"❤️ Здоровье: {self.hp}\n"
            f"⚔️ Атака: {self.attack_power}\n"
            f"🛡️ Защита: {self.defense}\n"
            f"🧠 Способности: {self.abilities}"
        )

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
# Создание подклассов для волшебника
class Wizard(Pokemon):
    def attack(self, enemy):
        return f"Покемон-Волшебник использует магическую атаку!", super().attack(enemy)

# Создание подклассов для бойца
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(100, 1000)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"Покемон-Боец наносит мощный удар!"