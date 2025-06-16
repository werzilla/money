from random import randint
import requests
from datetime import datetime, timedelta
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.last_feed_time = datetime.now()
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.health =randint(200,400)
        self.power = randint(20,60)
        

        Pokemon.pokemons[pokemon_trainer] = self


    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]['offical-artwork']["front_default"])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    
    def get_health(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code ==200 
            data = response.json()
            return (data['forms'][0]['health'])
        else:
            return "Pikachu"


    def get_power(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 20:
            data = response.json()
            return (data['forms'][0]['power'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
        Сила покемона: {self.power}
        Здоровье покемона: {self.health}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"""Сражение @{self.pokemon_trainer} c @{enemy.pokemon_trainer}
Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}"""
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"

    def feed(self, feed_interval = 60, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"
class Wizard(Pokemon):
    def feed(self):
        return super().feed(hp_increase=20)

    def info(self): 
        return "У тебя покемон-волшебник \n\n" + super().info()

class Fighter(Pokemon):
    def attack (self, enemy):
        super_power = randint(5,15)
        self_power += super_power
        result = super().attack(enemy)
        self_power += super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power}"
    def feed(self):
        return super().feed(feed_interval=10)

    def info(self): 
        return "У тебя покемон-боец \n\n" + super().info() 

