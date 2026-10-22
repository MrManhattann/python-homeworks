
class Device:
    def __init__(self, name, brand, power):
        self.name = name
        self.brand = brand
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} увімкнено.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} вимкнено.")

    def display_info(self):
        print(f"Пристрій: {self.name}")
        print(f"Виробник: {self.brand}")
        print(f"Потужність: {self.power} Вт")
        print(f"Стан: {'увімкнений' if self.is_on else 'вимкнений'}")


class CoffeeMachine(Device):
    def __init__(self, brand, power, coffee_type, water_tank):
        super().__init__("Кавомашина", brand, power)
        self.coffee_type = coffee_type
        self.water_tank = water_tank

    def make_coffee(self):
        if self.is_on:
            print(f"Готуємо каву: {self.coffee_type}.")
        else:
            print("Спочатку увімкніть кавомашину.")

    def display_info(self):
        super().display_info()
        print(f"Тип кави: {self.coffee_type}")
        print(f"Об'єм резервуара: {self.water_tank} л")


class Blender(Device):
    def __init__(self, brand, power, speeds):
        super().__init__("Блендер", brand, power)
        self.speeds = speeds

    def blend(self):
        if self.is_on:
            print("Блендер подрібнює продукти.")
        else:
            print("Спочатку увімкніть блендер.")

    def display_info(self):
        super().display_info()
        print(f"Кількість швидкостей: {self.speeds}")


class MeatGrinder(Device):
    def __init__(self, brand, power, productivity):
        super().__init__("М'ясорубка", brand, power)
        self.productivity = productivity

    def grind_meat(self):
        if self.is_on:
            print("М'ясорубка перемелює м'ясо.")
        else:
            print("Спочатку увімкніть м'ясорубку.")

    def display_info(self):
        super().display_info()
        print(f"Продуктивність: {self.productivity} кг/хв")


coffee_machine = CoffeeMachine("DeLonghi", 1450, "Еспресо", 1.8)
blender = Blender("Philips", 600, 5)
meat_grinder = MeatGrinder("Bosch", 500, 2)

coffee_machine.display_info()
coffee_machine.turn_on()
coffee_machine.make_coffee()

print()

blender.display_info()
blender.turn_on()
blender.blend()

print()

meat_grinder.display_info()
meat_grinder.turn_on()
meat_grinder.grind_meat()
