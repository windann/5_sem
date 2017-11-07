# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False,**kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.items = items
        self.ignore_case = ignore_case

        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']

        self.returned = set()

    def __next__(self):
        # Нужно реализовать __next__

        for item in self.items:
            if type(item) == str and self.ignore_case == True:
                if item.lower() not in self.returned:
                    self.returned.add(item.lower())
                    return item
            else:
                if item not in self.returned:
                    self.returned.add(item)
                    return item
        raise StopIteration()

    def __iter__(self):
        return self