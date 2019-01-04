# -*- coding: utf-8 -*-
from typing import List


def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                made_swap = True
        if not made_swap:
            break


def select_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        made_swap = False
        for j in range(i + 1, length):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                made_swap = True
        if not made_swap:
            break


def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        v = list[i]
        j = i - 1
        while j >= 0 and v < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = v


if __name__ == '__main__':
    list = [8, 1, 3, 2, 7, 4, 6, 9, 5]
    # bubble_sort(list)
    # select_sort(list)
    insertion_sort(list)
    print(list)
