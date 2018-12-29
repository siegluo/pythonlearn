# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_sore(t):
    return -t[1]


L1 = sorted(L, key=by_name)
print(L1)
L2 = sorted(L, key=by_sore)
print(L2)
