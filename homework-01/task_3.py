def palindromes(start, end):
    for number in range(start, end + 1):
        if str(number) == str(number)[::-1]:
            yield number


start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

print("Паліндроми:")

for number in palindromes(start, end):
    print(number)