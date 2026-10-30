
from product import Product


class ProductModel:
    def __init__(self):
        self.products = [
            Product(
                "Apple iPhone 16",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600",
                35999,
                4.9,
                1
            ),
            Product(
                "MacBook Air",
                "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600",
                52999,
                4.8,
                2
            ),
            Product(
                "Навушники",
                "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600",
                2499,
                4.7,
                3
            ),
            Product(
                "Фотоапарат",
                "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=600",
                18999,
                4.6,
                4
            )
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product

        return None

    def create_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можна додавати тільки об'єкти класу Product.")

        if product.id is None:
            product.id = max(
                (item.id for item in self.products),
                default=0
            ) + 1

        self.products.append(product)
        return product
