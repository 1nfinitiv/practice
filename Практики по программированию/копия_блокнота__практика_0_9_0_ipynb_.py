# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.9.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12on1rBYSFY84woG7-ISHMt5VFS_AXOfW

ФИО
"""



"""# Дисклеймер

В данной практике вам необходимо применить все ваши знания по темам:

- Функции
- Словари
- Списки
- Множества
- Условные конструкции
- Запросы

и все что было изучено на прошлых практических занятиях

В каждом задании кратко описаны функции, которые необходимо реализовать, детали реализации вы должны продумать самостоятельно

# Задание 0

Создайте функцию по нахождению уникальных элементов из двух списков



```
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
```
"""

def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    unique_in_list1 = set1 - set2
    unique_in_list2 = set2 - set1

    unique_elements = unique_in_list1.union(unique_in_list2)

    return list(unique_elements)


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique = unique_elements(list1, list2)
print("Уникальные элементы:", unique)

"""# Задание 1

Симулятор виртуального питомца

Цель: создать виртуальный симулятор домашних животных, в котором пользователи смогут заводить питомцев и ухаживать за ними.

Требования:

- Функция для усыновления питомца (имя, тип, возраст).
- Функция для того, чтобы покормить питомца, поиграть с ним или уложить его спать.
- Функция для отображения состояния питомца (голод, радость, энергия).
"""

import random


# Функция для усыновления питомца
def adopt_pet(name, pet_type, age):
    return {
        'name': name,
        'type': pet_type,
        'age': age,
        'hunger': 5,
        'happiness': 5,
        'energy': 5
    }


# Функция для кормления питомца
def feed_pet(pet):
    if pet['hunger'] < 10:
        pet['hunger'] += 1
        print(f"{pet['name']} накормлен!")
    else:
        print(f"{pet['name']} уже сытый!")


# Функция для игры с питомцем
def play_with_pet(pet):
    if pet['energy'] > 0:
        pet['energy'] -= 1
        pet['happiness'] += 1
        pet['hunger'] += random.choice([-1, 0, 1])  # Игры могут немного увеличить или уменьшить голод
        print(f"Вы поиграли с {pet['name']}!")
    else:
        print(f"{pet['name']} слишком устал для игры!")


# Функция для укладывания питомца спать
def put_pet_to_sleep(pet):
    pet['energy'] += 2
    print(f"{pet['name']} уснул. Энергия восстановлена!")


# Функция для отображения состояния питомца
def display_pet_status(pet):
    print(f"Имя: {pet['name']}")
    print(f"Тип: {pet['type']}, Возраст: {pet['age']} лет")
    print(f"Голод: {pet['hunger']}/10")
    print(f"Радость: {pet['happiness']}/10")
    print(f"Энергия: {pet['energy']}/10")


# Пример использования
pet = adopt_pet("Соска", "собака", 2)

while True:
    display_pet_status(pet)
    action = input("Что вы хотите сделать? (поесть/играть/спать/выход): ").strip().lower()

    if action == "поесть":
        feed_pet(pet)
    elif action == "играть":
        play_with_pet(pet)
    elif action == "спать":
        put_pet_to_sleep(pet)
    elif action == "выход":
        print("Питомец умер")
        break
    else:
        print("Неверное действие!")

"""# Задание 2

Рыцарь и дракон

Цель: создать небольшую игру, в которой вам необходимо играть за рыцаря и сразиться с драконом

Требования:

- Создание персонажа (имя, информация о доспехах, оружии, урон, здоровье)
- Управление персонажем и мини сюжет
- Создание дракона (Имя, информация о здоровье и уроне)
- Боевая система (нанесение и получение урона, урон должен быть случайным в заданном диапазоне)
- Реализовать бой между драконом и рыцарем
"""

import random


# Функция для создания персонажа
def create_knight():
    name = input("Введите имя рыцаря: ")
    armor = input("Введите информацию о доспехах: ")
    weapon = input("Введите информацию об оружии: ")
    damage = random.randint(5, 15)  # Урон рыцаря в диапазоне
    health = 100  # Здоровье рыцаря
    return {"name": name, "armor": armor, "weapon": weapon, "damage": damage, "health": health}


# Функция для создания дракона
def create_dragon():
    name = "Дракон"
    health = 100  # Здоровье дракона
    damage = random.randint(8, 20)  # Урон дракона в диапазоне
    return {"name": name, "health": health, "damage": damage}


# Функция для боя между рыцарем и драконом
def battle(knight, dragon):
    while knight["health"] > 0 and dragon["health"] > 0:
        # Определение, кто атакует
        knight_attack_roll = random.randint(1, 6)  # Бросок кубика для рыцаря
        dragon_attack_roll = random.randint(1, 6)  # Бросок кубика для дракона

        if knight_attack_roll > dragon_attack_roll:
            # Рыцарь атакует дракона
            damage_dealt = random.randint(1, knight["damage"])  # Случайный урон рыцаря
            dragon["health"] -= damage_dealt
            print(f"{knight['name']} атакует {dragon['name']} на {damage_dealt} урона.")
        else:
            # Дракон атакует рыцаря
            damage_dealt = random.randint(1, dragon["damage"])  # Случайный урон дракона
            knight["health"] -= damage_dealt
            print(f"{dragon['name']} атакует {knight['name']} на {damage_dealt} урона.")

        # Вывод текущего состояния здоровья
        print(f"Здоровье {knight['name']}: {knight['health']}")
        print(f"Здоровье {dragon['name']}: {dragon['health']}")
        print("---")

    # Определение победителя
    if knight["health"] > 0:
        print(f"{knight['name']} победил {dragon['name']}!")
    else:
        print(f"{dragon['name']} победил {knight['name']}!")


print("Добро пожаловать в игру 'Рыцарь и дракон'!")

knight = create_knight()
dragon = create_dragon()

print("")

print(f"Ваш рыцарь: {knight['name']} (Здоровье: {knight['health']}, Урон: {knight['damage']})")
print(f"Враг, дракон: {dragon['name']} (Здоровье: {dragon['health']}, Урон: {dragon['damage']})")

battle(knight, dragon)

"""# Задание 3

Цель - создать менеджера команды Pokémon, который позволит пользователям:

- Добавлять покемонов в свою команду. (если такого покемона еще нет в команде)
- Удалять покемонов из их команды.
- Просматривать подробную информацию обо всех покемонах в команде.
- Находить покемона по имени.
- Устраивать тренировочный бой между двумя покемонами

Для данной задачи используйте: https://pokeapi.co/
"""

