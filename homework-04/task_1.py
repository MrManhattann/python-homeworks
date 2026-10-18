
from datetime import date


class Book:
    def __init__(self, title, author, year, pages):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Назва книги не може бути порожньою.")

        if not isinstance(author, str) or not author.strip():
            raise ValueError("Ім'я автора не може бути порожнім.")

        if not isinstance(year, int) or isinstance(year, bool):
            raise ValueError("Рік видання повинен бути цілим числом.")

        if year < 1 or year > date.today().year:
            raise ValueError("Некоректний рік видання.")

        if not isinstance(pages, int) or isinstance(pages, bool):
            raise ValueError("Кількість сторінок повинна бути цілим числом.")

        if pages < 0:
            raise ValueError("Кількість сторінок не може бути від'ємною.")

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return (
            f'"{self.title}" — {self.author}, '
            f'{self.year} рік, {self.pages} сторінок'
        )

    def __repr__(self):
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"year={self.year!r}, pages={self.pages!r})"
        )

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return (
            self.title.casefold() == other.title.casefold()
            and self.author.casefold() == other.author.casefold()
        )

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.pages < other.pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.pages + other.pages

    def __contains__(self, word):
        if not isinstance(word, str):
            return False

        return word.casefold() in self.title.casefold()

    def __bool__(self):
        return self.pages > 0


book1 = Book("Кобзар", "Тарас Шевченко", 1840, 320)
book2 = Book("Лісова пісня", "Леся Українка", 1911, 96)
book3 = Book("Кобзар", "Тарас Шевченко", 1840, 320)
book4 = Book("Порожня книга", "Невідомий автор", 2020, 0)

print("Інформація про книги:")
print(book1)
print(book2)

print("\nПредставлення для налагодження:")
print(repr(book1))

print("\nКількість сторінок першої книги:", len(book1))

print("\nЧи однакові перша і третя книги?", book1 == book3)

print("Чи друга книга коротша за першу?", book2 < book1)

print("Сумарна кількість сторінок:", book1 + book2)

print('Чи є слово "Кобзар" у назві першої книги?', "Кобзар" in book1)
print('Чи є слово "лісова" у назві другої книги?', "лісова" in book2)


books = [book1, book2, book3]
sorted_books = sorted(books)

print("\nКниги, відсортовані за кількістю сторінок:")
for book in sorted_books:
    print(book)


print("\nЧи перша книга непорожня?", bool(book1))
print("Чи четверта книга непорожня?", bool(book4))


print("\nПеревірка некоректних даних:")

try:
    invalid_book = Book("Помилкова книга", "Автор", 2020, -10)
except ValueError as error:
    print("Помилка:", error)

try:
    invalid_book = Book("Майбутнє", "Автор", 2030, 100)
except ValueError as error:
    print("Помилка:", error)
