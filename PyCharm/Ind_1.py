#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов.

4.1:
Парой называется класс с двумя полями, которые обычно имеют имена first и second. Требуется
реализовать тип данных с помощью такого класса. Во всех заданиях обязательно должны
присутствовать:
    метод инициализации __init__ ; метод должен контролировать значения аргументов на
корректность;
    ввод с клавиатуры read ;
    вывод на экран display .
Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры.
Функция должна получать в качестве аргументов значения для полей структуры и возвращать
структуру требуемого типа. При передаче ошибочных параметров следует выводить сообщение
и заканчивать работу.
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся
после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.

8. Поле first — целое число, левая граница диапазона, включается в диапазон; поле second —
целое число, правая граница диапазона, не включается в диапазон. Пара чисел
представляет полуоткрытый интервал [first, second). Реализовать метод rangecheck() —
проверку заданного целого числа на принадлежность диапазону.
"""


def is_number(a):
    try:
        float(a)
    except ValueError:
        return False
    return True


class Coordinates:
    # Конструктор класса.
    def __init__(self, first=0.0, second=0.0):
        if is_number(first) and is_number(second):
            if first > 0 and second > 0:
                self.first = first
                self.second = second
        else:
            raise ValueError

    def read(self):
        self.first = float(input("Enter the first value: "))
        self.second = float(input("Enter the second value: "))

    # Переопределение метода, вызываемого при использовании оператора in для объекта класса.
    # Возвращает True, если значение x входит в интервал [self.first, self.second),
    # и False в противном случае
    def __contains__(self, x):
        return self.first <= x < self.second

    # Метод, который выводит на экран сообщение о том, принадлежит ли число x интервалу
    def rangecheck(self, x):
        if x in self:  # Если число x входит в интервал [self.first, self.second),
            print(f"{x} принадлежит диапазону [{self.first}, {self.second})")
        else:
            print(f"{x} не принадлежит диапазону [{self.first}, {self.second})")

    # Метод, вызываемый при использовании функции print() для объекта класса.
    # Возвращает строковое представление объекта класса.
    def __repr__(self):
        return f"{self.__class__.__name__}({self.first}, {self.second})"


# Пример использования класса Coordinates
if __name__ == '__main__':
    p = Coordinates(2, 10)

    p1 = Coordinates()
    p1.read()
    print(p1)

    print(p)

    print(p.first)
    print(p.second)

    print(5 in p)

    p.rangecheck(5)
    p.rangecheck(10)
