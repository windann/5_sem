import datetime
from collections import Counter

def get_age(birthday):
    """Получение возраста из даты рождения"""
    today = datetime.date.today()
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1
    return age

def get_histogram(list):
    """Получение словаря с количеством людей определённого возраста"""
    sorted_dict = Counter(sorted(list))
    return dict(sorted_dict)

def print_histogram(dict):
    """Печать гистограммы"""
    for key,values in dict.items():
        print(str(key) + ' ' + '#' * values)
