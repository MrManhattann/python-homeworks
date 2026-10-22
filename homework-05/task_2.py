
class Ship:
    def __init__(self, name, displacement, max_speed):
        self.name = name
        self.displacement = displacement
        self.max_speed = max_speed

    def sail(self):
        print(f"Корабель {self.name} вирушив у плавання.")

    def display_info(self):
        print(f"Назва корабля: {self.name}")
        print(f"Водотоннажність: {self.displacement} тонн")
        print(f"Максимальна швидкість: {self.max_speed} вузлів")


class Frigate(Ship):
    def __init__(self, name, displacement, max_speed, crew):
        super().__init__(name, displacement, max_speed)
        self.crew = crew

    def patrol(self):
        print(f"Фрегат {self.name} виконує патрулювання.")

    def display_info(self):
        super().display_info()
        print(f"Екіпаж: {self.crew} осіб")
        print("Тип корабля: фрегат")


class Destroyer(Ship):
    def __init__(self, name, displacement, max_speed, missile_count):
        super().__init__(name, displacement, max_speed)
        self.missile_count = missile_count

    def defend(self):
        print(f"Есмінець {self.name} виконує завдання із захисту.")

    def display_info(self):
        super().display_info()
        print(f"Кількість ракет: {self.missile_count}")
        print("Тип корабля: есмінець")


class Cruiser(Ship):
    def __init__(self, name, displacement, max_speed, range_km):
        super().__init__(name, displacement, max_speed)
        self.range_km = range_km

    def perform_mission(self):
        print(f"Крейсер {self.name} виконує морську місію.")

    def display_info(self):
        super().display_info()
        print(f"Дальність плавання: {self.range_km} км")
        print("Тип корабля: крейсер")


frigate = Frigate("Гетьман Сагайдачний", 3500, 30, 180)
destroyer = Destroyer("Морський захисник", 9000, 32, 48)
cruiser = Cruiser("Адмірал", 12000, 29, 8000)

frigate.display_info()
frigate.sail()
frigate.patrol()

print()

destroyer.display_info()
destroyer.sail()
destroyer.defend()

print()

cruiser.display_info()
cruiser.sail()
cruiser.perform_mission()
