
class Book:
    def __init__(self, title="", year=0, publisher="", genre="",
                 author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Введіть назву книги: ")
        self.year = int(input("Введіть рік видання: "))
        self.publisher = input("Введіть видавця: ")
        self.genre = input("Введіть жанр книги: ")
        self.author = input("Введіть автора: ")
        self.price = float(input("Введіть ціну книги: "))

    def display_info(self):
        print("\n--- Інформація про книгу ---")
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price:.2f} грн")

    def change_price(self, new_price):
        self.price = new_price
        print("Ціну книги змінено.")


book = Book()
book.input_data()
book.display_info()

new_price = float(input("\nВведіть нову ціну книги: "))
book.change_price(new_price)
book.display_info()
