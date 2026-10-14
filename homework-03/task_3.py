
class Stadium:
    def __init__(self, name="", opening_date="", country="", city="",
                 capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Введіть дату відкриття: ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість стадіону: "))

    def display_info(self):
        print("\n--- Інформація про стадіон ---")
        print(f"Назва: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} осіб")

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        print("Місткість стадіону змінено.")


stadium = Stadium()
stadium.input_data()
stadium.display_info()

new_capacity = int(input("\nВведіть нову місткість стадіону: "))
stadium.change_capacity(new_capacity)
stadium.display_info()
