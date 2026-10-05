def multiples_of_five(start, end):
    for number in range(start, end + 1):
        if number % 5 == 0:
            yield number


start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

print("Числа, кратні п'яти:")

for number in multiples_of_five(start, end):
    print(number)