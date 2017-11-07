#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = None

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open('data_light.json') as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(sorted(unique(field(arg, 'job-name'), ignore_case=True)))

@print_result
def f2(arg):
    return list(filter(lambda line: line.startswith('Программист') or line.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda line: line + ' с опытом Python',arg))



@print_result
def f4(arg):
    random = list(gen_random(100000,200000,len(arg)))
    salary = list(map(lambda line:', зарплата ' + str(line) + ' руб' , random))

    return list(map(lambda y: y[0] + y[1], zip(arg, salary)))


with timer():
    f4(f3(f2(f1(data))))




