import random
 
 
class SpaceShip:
    def __init__(self, fuel=100, hull=100, speed=0):
        self.fuel = fuel
        self.hull = hull
        self.speed = speed
 
    def accelerate(self, delta: int):
        """ Ускоряет корабль, расходуя топливо (0.5 на единицу скорости). """
        cost = delta * 0.5
        if self.fuel < cost:
            print("Не хватает топлива!")
            return
        self.fuel -= cost
        self.speed += delta
 
    def take_damage(self, damage: int):
        """ Наносит урон кораблю. """
        self.hull = max(0, self.hull - damage)
 
    def __str__(self):
        return f"Корабль: топливо {self.fuel} %, корпус {self.hull} %, скорость {self.speed}"
 
 
class CrewMember:
    def __init__(self, name: str, role: str, skill: int, health = 100):
        self.name = name
        self.role = role
        self.skill = skill
        self.health = health
 
    def __str__(self):
        return f"{self.name} ({self.role}): здоровье {self.health}, навыки {self.skill}"
    
class Event:
    def __init__(self, name: str, damage: int):
        """ Возможное событие миссии с собственным уроном. """
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} (урон {self.damage})"
 
 
class Mission:
    def __init__(self, goal: str, events: list):
        self.goal = goal
        self.events = events
 
    def run(self, ship: SpaceShip, crew: list):
        """ Выполняет миссию: ускоряет корабль, применяет случайное событие, ранит экипаж. """
        print(f"Миссия: {self.goal}")
        ship.accelerate(50)
        event = random.choice(self.events)
        print(f"Событие: {event.name} (урон {event.damage})")
        ship.take_damage(event.damage)
        for member in crew:
            member.health -= 10
 
 
ship = SpaceShip()
crew = [CrewMember("Анна", "пилот", 80), CrewMember("Олег", "инженер", 70)]
Mission("Долететь до Марса", [Event("авария", 20), Event("астероиды", 15)]).run(ship, crew)
 
print(ship)
for member in crew:
    print(member)
    