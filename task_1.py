# Нужно реализовать функцию, принимающую список чисел.
# Вывести число, которое встречается чаще всего.
# Максимальное число голосов всегда уникально.

import requests
def vote(votes):
    k = 0
    max = 0
    for i in votes:
      c = votes.count(i)
      if c > max:
        max = c
        res = i
    return res

# Напишите программу, которая проверяет длины трёх сторон треугольника (side1, side2, side3)
# и определяет его тип: “Равносторонний треугольник”, “Равнобедренный треугольник” или “Разносторонний треугольник”.
# В случае некорректных величин значения сторон (0 или отрицательное значение), вывод должен быть – “Треугольник не существует”.


def check_triangle(side1: int, side2: int, side3: int):
    if side1 <= 0 or side2<= 0 or side3 <= 0 or side1+side2 <= side3 or side1+side3<= side2 or side2+side3<=side1:
        result = "Треугольник не существует"
    elif side1==side2==side3:
        result = "Равносторонний треугольник"
    elif side1==side2!=side3 or side1 == side3!=side2 or side2==side3!=side1:
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result

# Напишите программу, которая проверяет логин (переменная login) и пароль (переменная password) пользователя.
# Если логин равен “admin” и пароль равен “password”, выведите сообщение «Добро пожаловать»,
# иначе выведите сообщение «Доступ ограничен».


def check_auth(login: str, password: str):

    if login == "admin" and password == "password":
        result = "Добро пожаловать"
        return result
    else:
        result = "Доступ ограничен"
        return result

    return result

