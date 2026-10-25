
import json


class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class JsonMixin:
    def to_json(self):
        return json.dumps(
            {
                "name": self.name,
                "price": self.price
            },
            ensure_ascii=False,
            indent=4
        )


class DiscountMixin:
    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Знижка повинна бути від 0 до 100%.")

        discounted_price = self.price * (1 - percent / 100)
        return round(discounted_price, 2)


class Product:
    def __init__(self, name, price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Назва товару не може бути порожньою.")

        if price < 0:
            raise ValueError("Ціна не може бути від'ємною.")

        self.name = name
        self.price = price


class ProductManager(
    LoggingMixin,
    JsonMixin,
    DiscountMixin,
    Product
):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.log(f"Створено товар: {self.name}, ціна {self.price} грн")

    def display_info(self):
        print(f"Назва товару: {self.name}")
        print(f"Ціна: {self.price} грн")



product = ProductManager("Навушники", 1000)

print("\nІнформація про товар:")
product.display_info()


print("\nПеревірка логування:")
product.log("Перевірка роботи системи.")


print("\nТовар у форматі JSON:")
print(product.to_json())

print("\nЗастосування знижки:")
discounted_price = product.apply_discount(15)
print(f"Ціна до знижки: {product.price} грн")
print(f"Знижка: 15%")
print(f"Ціна після знижки: {discounted_price} грн")

print("\nПорядок пошуку методів (MRO):")
for cls in ProductManager.mro():
    print(cls.__name__)
