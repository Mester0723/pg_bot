from random import randint
import requests

class Pokemon:
    pokemons = {}
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

        Pokemon.pokemons[pokemon_trainer] = self

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