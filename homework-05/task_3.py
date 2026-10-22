
class Money:
    def __init__(self, whole_part, fractional_part):
        if whole_part < 0 or fractional_part < 0:
            raise ValueError("Сума не може бути від'ємною.")

        total_kopecks = whole_part * 100 + fractional_part
        self.whole_part = total_kopecks // 100
        self.fractional_part = total_kopecks % 100

    def set_amount(self, whole_part, fractional_part):
        if whole_part < 0 or fractional_part < 0:
            raise ValueError("Сума не може бути від'ємною.")

        total_kopecks = whole_part * 100 + fractional_part
        self.whole_part = total_kopecks // 100
        self.fractional_part = total_kopecks % 100

    def get_total_kopecks(self):
        return self.whole_part * 100 + self.fractional_part

    def display(self):
        print(f"{self.whole_part} грн {self.fractional_part:02d} коп.")

    def __str__(self):
        return f"{self.whole_part} грн {self.fractional_part:02d} коп."


class Product(Money):
    def __init__(self, name, whole_part, fractional_part):
        super().__init__(whole_part, fractional_part)
        self.name = name

    def decrease_price(self, whole_part, fractional_part):
        if whole_part < 0 or fractional_part < 0:
            raise ValueError("Зменшення ціни не може бути від'ємним.")

        reduction = whole_part * 100 + fractional_part
        current_price = self.get_total_kopecks()

        if reduction > current_price:
            raise ValueError("Зменшення не може перевищувати ціну товару.")

        new_price = current_price - reduction
        self.set_amount(new_price // 100, new_price % 100)

    def display(self):
        print(f"Товар: {self.name}")
        print(f"Ціна: {self}")


money = Money(125, 75)

print("Початкова сума:")
money.display()

money.set_amount(200, 50)
print("Змінена сума:")
money.display()

# Перевірка роботи класу Product
product = Product("Навушники", 1500, 99)

print("\nІнформація про товар:")
product.display()

product.decrease_price(200, 50)

print("\nЦіна після знижки:")
product.display()
