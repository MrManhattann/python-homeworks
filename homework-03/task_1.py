
class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0,
                 color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Введіть модель автомобіля: ")
        self.year = int(input("Введіть рік випуску: "))
        self.manufacturer = input("Введіть виробника: ")
        self.engine_volume = float(input("Введіть об'єм двигуна (л): "))
        self.color = input("Введіть колір автомобіля: ")
        self.price = float(input("Введіть ціну автомобіля: "))

    def display_info(self):
        print("\n--- Інформація про автомобіль ---")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price:.2f} грн")

    def change_price(self, new_price):
        self.price = new_price
        print("Ціну автомобіля змінено.")


car = Car()
car.input_data()
car.display_info()

new_price = float(input("\nВведіть нову ціну автомобіля: "))
car.change_price(new_price)
car.display_info()
