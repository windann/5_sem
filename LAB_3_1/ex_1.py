#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
print(', ' .join(field(goods,'title')))

print(' '.join(map(str, field(goods, 'title', 'price','color'))))

print(', '.join(map(str, gen_random(1, 3, 5))))


