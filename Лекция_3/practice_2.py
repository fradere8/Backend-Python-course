class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        
    def get_info(self):
        """ Возвращает основную информацию об автомобиле. """
        return f"{self.make} {self.model} {self.year} года выпуска."
    
    def start_engine(self):
        """ Запускает двигатель и возвращает сообщение о результате. """
        return "Двигатель запущен."
    
    def stop_engine(self):
        """ Останавливает двигатель и возвращает сообщение о результате. """
        return "Двигатель остановлен."
    
class SportsCar(Car):
    def __init__(self, make: str, model: str, year: int, top_speed: int, has_turbo: bool):
        super().__init__(make, model, year)
        self.top_speed = top_speed
        self.has_turbo = has_turbo

    def get_info(self):
        """ Возвращает информацию о спорткаре. """
        return f"{self.make} {self.model} {self.year} года выпуска. Максимальная скорость: {self.top_speed} км/ч. " \
               f"{'Оборудован турбиной' if self.has_turbo else 'Не оборудован турбиной'}."

class OffRoadCar(Car):
    def __init__(self, make: str, model: str, year: int, ground_clearance: int, has_4wd: bool):
        super().__init__(make, model, year)
        self.ground_clearance = ground_clearance
        self.has_4wd = has_4wd

    def get_info(self):
        """ Возвращает информацию о внедорожнике. """
        return f"{self.make} {self.model} {self.year} года выпуска. Клиренс: {self.ground_clearance}. " \
            f"{'Есть полный привод' if self.has_4wd else 'Нет полного привода'}."
                
class LuxuryCar(Car):
    def __init__(self, make: str, model: str, year: int, interior_material: str, has_autopilot: bool):
        super().__init__(make, model, year)
        self.interior_material = interior_material
        self.has_autopilot = has_autopilot

    def get_info(self):
        """ Возвращает информацию об автомобиле класса люкс. """
        return f"{self.make} {self.model} {self.year} года выпуска. Материал интерьера: {self.interior_material}. " \
            f"{'Есть автопилот' if self.has_autopilot else 'Нет автопилота'}."
                
cars = [
    SportsCar('Ferrari', '488 GTB', 2020, 330, True),
    OffRoadCar('Jeep', 'Wrangler', 2019, 27, True),
    LuxuryCar('Mercedes-Benz', 'S-Class', 2021, 'кожа', True)
]

for car in cars:
    print(car.get_info())