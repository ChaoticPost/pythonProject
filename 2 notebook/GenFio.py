import math
import random

file_surnames = r'C:\Users\фвьшт\PycharmProjects\pythonProject\2 notebook\sun'
file_names = r'C:\Users\фвьшт\PycharmProjects\pythonProject\2 notebook\name'


def generate_surname():
    surnames = random.sample(list(open(file_surnames, encoding="UTF-8")), k=2)
    surname1 = surnames[0].strip()
    surname2 = surnames[1].strip()
    return surname1[:get_middle_index(surname1):] + surname2[get_middle_index(surname2)::]


def generate_full_name():
    name = random.choice(list(open(file_names, encoding="UTF-8"))).strip()
    initial = random.choice('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
    surname = generate_surname()
    return f"{name} {initial}. {surname}"


def get_middle_index(s):
    return math.floor(len(s) / 2)


print(generate_full_name())