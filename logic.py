from random import randint
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
        self.attack = randint(20, 100)
        self.defense = randint(10, 80)
        self.type = self.get_type()
        self.abilities = self.get_abilities()
        self.level = 1
        self.exp = 0
        self.feed_count = 0
        Pokemon.achievements.setdefault(pokemon_trainer, [])

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для кормления покемона
    def feed(self, food=10):
        self.hp = min(self.hp + food, 200)
        self.feed_count += 1
        self.exp += 5
        self.check_level_up()
        self.check_achievements()
        return f"{self.name} покормлен! HP: {self.hp}, опыт: {self.exp}"

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

    # Метод класса для получения информации
    def info(self):
        return (
            f"👾 Имя покемона: {self.name}\n"
            f"🔷 Тип: {self.type}\n"
            f"❤️ Здоровье: {self.hp}\n"
            f"⚔️ Атака: {self.attack}\n"
            f"🛡️ Защита: {self.defense}\n"
            f"🧠 Способности: {self.abilities}"
        )

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
