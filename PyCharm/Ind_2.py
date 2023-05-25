#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать метод
size(), возвращающий установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения size и count
устанавливаются конструктором.
В тех задачах, где возможно, реализовать конструктор инициализации строкой.


8. Реализовать класс Money, используя для представления суммы денег список словарей.
Словарь имеет два ключа: номинал купюры и количество купюр данного достоинства.
Номиналы представить как строку. Элемент списка словарей с меньшим индексом
содержит меньший номинал.
"""


class Money:
    # константа для максимального размера списка словарей
    MAX_SIZE = 10

    # конструктор класса
    def __init__(self, n=None):
        self.count = 0
        self._size = Money.MAX_SIZE
        self.money_list = []  # список словарей

        # если передана строка, инициализируем список словарей соответствующим образом
        # isinstance - Позволяет проверить принадлежность экземпляра к классу.
        if isinstance(n, str):
            denominations = n.split(", ")
            for d in denominations:
                money = d.split(": ")
                if money[0].isnumeric() and money[1].isnumeric():
                    denomination = int(money[0])
                    number = int(money[1])
                    if self.count < self._size:
                        self.money_list.append({"denomination": str(denomination), "number": number})
                        self.count += 1

        # иначе инициализируем список словарей нулями
        else:
            for i in range(self.count):
                self.money_list.append({"denomination": str(i), "number": 0})

        # сортировка списка по номиналу
        self.money_list = sorted(self.money_list, key=lambda d: int(d['denomination']))

    # перегрузка операции индексирования
    def __getitem__(self, index):
        if 0 <= index <= self.count:
            return self.money_list[index]
        else:
            raise IndexError("Index out of range")

    # метод, возвращающий установленную длину
    def get_size(self):
        return self.count

    # метод, добавляющий количество купюр заданного номинала
    def add(self, denomination, number):
        for item in self.money_list:
            if item["denomination"] == str(denomination):
                item["number"] += number
                return
        # если номинал не найден, добавляем словарь в список
        if self.count < self._size:
            self.money_list.append({"denomination": str(denomination), "number": number})
            self.count += 1
        else:
            raise ValueError("List is full")

    # метод, удаляющий количество купюр заданного номинала
    def remove(self, denomination, number):
        for item in self.money_list:
            if item["denomination"] == str(denomination):
                if item["number"] >= number:
                    item["number"] -= number
                    if item["number"] == 0:
                        self.money_list.remove(item)
                        self.count -= 1
                    return
                else:
                    raise ValueError("Not enough money")
        raise ValueError("Denomination not found")

    # метод, возвращающий общую сумму денег
    def total(self):
        total_sum = 0
        for item in self.money_list:
            total_sum += int(item["denomination"]) * item["number"]
        return total_sum

    # метод для удобного вывода на экран содержимого объекта
    def __repr__(self):
        return ", ".join([f"{item['denomination']}: {item['number']}" for item in self.money_list])


# Пример использования класса Money
if __name__ == '__main__':
    # инициализация объекта класса с помощью строки
    m = Money("100: 10, 50: 5, 10: 20, 200: 1")

    # вывод количества элементов списка словарей
    print(m.get_size())

    # вывод общей суммы денег
    print(m.total())

    # вывод содержимого объекта
    print(m)
    # добавление и удаление купюр
    m.add(20, 5)
    print(m)

    m.remove(100, 5)
    print(m)

    # использование операции индексирования
    print(m[0])
    # print(m[12])
    print(m[2])

    print('-' * 50)

    k = Money()
    print(k.get_size())
    print(k)
