from typing import List
import numpy as np
import string
# sentence = "Hello world have a nice day"
#
# sentence_list = str.split(sentence)
# print(sentence_list)
#
# length = 0
# for i,elem in enumerate(sentence_list):
#     if len(elem) > length:
#         length = len(elem)
#         idx = i
#
# print('Najdłuższy wyraz w liście to:', sentence_list[idx])
#
# liczby = [k for k in range(0,11,1)]
# print(liczby)
#
# suma = sum(liczby)
# średnia = suma/len(liczby)
#
# print(średnia)
#
# print(sum(liczby[2:4]))

dataset = {
    None: ValueError,
    123: ValueError,
    "": ValueError,
    " ": ValueError,
    "a ": False,
    "a b": False,
    "test": False,
    "a": False,
    "bb": True,
    "Bb": True,
    "abba": True,
    "ABba": True,
    "Do geese see God": True,
    "do geese see God": True,
    " do geese see God ": True,
    "12345": False,
    "11311": True,
    "Do geese see God?": True,
    "Race fast, safe car.": True,
    "Dammit, I'm mad.": True
}

# print(str.split("Race fast, safe car."))
# wyrzucić spacje, wyrzucić znaki interpunkcyjne, zmaienic duże litery na małe

def check_if_palindrom(element):

    if isinstance(element, str):
        if element in string.whitespace:
            raise ValueError('')
        else:
            lista = ''
            for i in element:
                if i not in string.whitespace and i not in string.punctuation:
                    lista += i
            if len(lista) == 1:
                return False

            lower_list = lista.lower()
            # print(lower_list)
            # lista_temp = list(lower_list)
            return lower_list == lower_list[::-1]

    else:
       raise ValueError('incorrect input')

result = check_if_palindrom(" do geese see God ")
print(result)

for value, expected_result in dataset.items():
    print("Test start: ", value)
    try:
        actual_result = check_if_palindrom(value)
    except Exception as ex:
        actual_result = type(ex)
    assert actual_result is expected_result, f"{value} should return {expected_result}, got {actual_result}!"
    print("Test passed", value)

# remove whitespaces and punctuation
    data = data.translate(data.maketrans('', '', string.whitespace + string.punctuation))


#!/usr/bin/python
# -*- coding: utf-8 -*-


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)


def find_left_point(tab):
    min_point = tab[0]
    for point in tab[1:]:
        if point.x < min_point.x:
            min_point = point
        elif point.x == min_point.x:
            if point.y < min_point.y:
                min_point = point
    return min_point


def orientation(p, q, r):
    zm = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if zm > 0:
        return "R"
    elif zm < 0:
        return "L"
    else:
        return "C"


def distance(p, q):
    return ((p.x - q.x) * (p.x - q.x) +
            (p.y - q.y) * (p.y - q.y))


def convexfull(tab, ver2=False):
    if len(tab) < 3:
        return tab

    p = find_left_point(tab)
    p_id = tab.index(p)
    result = [p]
    while True:
        q_id = (p_id + 1) % len(tab)
        q = tab[q_id]

        for r in tab:
            if ver2:
                if orientation(p, q, r) == "C":
                    if distance(p, q) < distance(p, r):
                        q = r
                elif orientation(p, q, r) == "R":
                    q = r
            else:
                if orientation(p, q, r) == "R":
                    q = r

        p = q
        p_id = tab.index(p)
        if p.x == result[0].x and p.y == result[0].y:
            break
        result.append(q)

    return result


if _name_ == "_main_":
    lst1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    lst2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]

    points = []
    for point in lst1:
        points.append(Point(point[0], point[1]))
    print(convexfull(points, ver2=True))

    points = []
    for point in lst2:
        points.append(Point(point[0], point[1]))
    print(convexfull(points, ver2=True))

