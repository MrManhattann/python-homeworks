def odd_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number


start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

print("Непарні числа:")

for number in odd_numbers(start, end):
    print(number)