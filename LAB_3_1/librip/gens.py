import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    # проверка, если не пройдена- исключение
    assert len(args) > 0
    # Необходимо реализовать генератор
    # raise AssertionError

    if len(args) == 1:
        for elem in items:
            for key in args:
                a = elem.get(key)
                if a is not None:
                    yield a

    else:
        new_dict = {}

        for elem in items:
            for key in args:
                a = elem.get(key)
                new_dict[key] = a

            yield new_dict


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки

def gen_random(begin, end, num_count):
    for num in range(num_count):
        yield random.randint(begin, end)


        # Необходимо реализовать генератор
