
def horizontal_line(symbol):
    print(symbol * 10)


def vertical_line(symbol):
    for _ in range(10):
        print(symbol)


def show_line(symbol, function_to_call):
    function_to_call(symbol)


symbol = input("Введіть символ для лінії: ")
line_type = input("Яку лінію показати? (горизонтальна/вертикальна): ").lower()

if line_type == "горизонтальна":
    show_line(symbol, horizontal_line)
elif line_type == "вертикальна":
    show_line(symbol, vertical_line)
else:
    print("Невідомий тип лінії!")
