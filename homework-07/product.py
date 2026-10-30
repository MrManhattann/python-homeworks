
class Product:
    def __init__(self, title, image, price, rating, product_id=None):
        self.id = product_id
        self.title = title
        self.image = image
        self.price = price
        self.rating = rating

    def __str__(self):
        return f"{self.title} — {self.price} грн"
