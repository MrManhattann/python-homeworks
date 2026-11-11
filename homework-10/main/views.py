
from datetime import date, timedelta

from django.shortcuts import render


# Демонстраційні облікові записи
USERS = {
    "admin": {
        "password": "admin123",
        "role": "Адміністратор",
    },
    "user": {
        "password": "user123",
        "role": "Звичайний користувач",
    },
}


# Завдання 1. Авторизація
def login_view(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = USERS.get(username)

        if user and user["password"] == password:
            context["success"] = True
            context["username"] = username
            context["role"] = user["role"]
        else:
            context["error"] = "Неправильний логін або пароль."

    return render(request, "main/login.html", context)


# Завдання 2. Калькулятор трьох чисел
def calculator_view(request):
    context = {}

    if request.method == "POST":
        try:
            number1 = float(request.POST.get("number1", ""))
            number2 = float(request.POST.get("number2", ""))
            number3 = float(request.POST.get("number3", ""))

            operation = request.POST.get("operation")

            if operation == "min":
                result = min(number1, number2, number3)
                operation_name = "Мінімальне число"

            elif operation == "max":
                result = max(number1, number2, number3)
                operation_name = "Максимальне число"

            elif operation == "average":
                result = (number1 + number2 + number3) / 3
                operation_name = "Середнє арифметичне"

            else:
                raise ValueError("Оберіть правильну операцію.")

            context["result"] = result
            context["operation_name"] = operation_name

        except (ValueError, TypeError):
            context["error"] = "Введіть три коректні числа та виберіть операцію."

    return render(request, "main/calculator.html", context)


# Завдання 3. Реєстрація в інтернет-магазині
def registration_view(request):
    context = {}

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        age = request.POST.get("age", "").strip()
        email = request.POST.get("email", "").strip()
        gender = request.POST.get("gender", "")
        address = request.POST.get("address", "").strip()
        newsletter = request.POST.get("newsletter") == "on"

        try:
            age_number = int(age)

            if not first_name or not last_name or not email or not address:
                raise ValueError

            if age_number < 1 or age_number > 120:
                raise ValueError

            if gender not in ["Чоловіча", "Жіноча", "Не хочу вказувати"]:
                raise ValueError

            context["registered"] = True
            context["first_name"] = first_name
            context["last_name"] = last_name
            context["age"] = age_number
            context["email"] = email
            context["gender"] = gender
            context["address"] = address
            context["newsletter"] = newsletter

        except ValueError:
            context["error"] = "Перевірте правильність введених даних."

    return render(request, "main/registration.html", context)


# Завдання 4. День програміста
def programmer_day_view(request):
    context = {}

    if request.method == "POST":
        try:
            year = int(request.POST.get("year", ""))

            if year < 1 or year > 9999:
                raise ValueError

            # День програміста — 256-й день року
            programmer_day = date(year, 1, 1) + timedelta(days=255)

            weekdays = [
                "понеділок",
                "вівторок",
                "середа",
                "четвер",
                "п'ятниця",
                "субота",
                "неділя",
            ]

            months = [
                "",
                "січня",
                "лютого",
                "березня",
                "квітня",
                "травня",
                "червня",
                "липня",
                "серпня",
                "вересня",
                "жовтня",
                "листопада",
                "грудня",
            ]

            context["result"] = (
                f"{programmer_day.day} "
                f"{months[programmer_day.month]} "
                f"({weekdays[programmer_day.weekday()]})"
            )
            context["year"] = year

        except ValueError:
            context["error"] = "Введіть коректний рік від 1 до 9999."

    return render(request, "main/programmer_day.html", context)
