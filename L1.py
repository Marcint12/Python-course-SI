from numpy.random import *
import numpy as np


def bubble(a):
    tab_size = np.size(a)
    tab = a.copy()
    w = 1
    while w != (tab_size-1):
        w = tab_size - 1
        for i in range(tab_size-1):
            if tab[i] > tab[i + 1]:
                w = w - 1
                b1 = tab[i]
                b2 = tab[i + 1]
                tab[i] = b2
                tab[i + 1] = b1
    return tab


def insertion_sort(a):
    tab_size = np.size(a)
    tab = [a[0]]
    for i in range(1, tab_size):
        for j in range(tab_size):
            if a[i] < tab[j]:
                tab.insert(j, a[i])
                break
            elif j == (np.size(tab)-1):
                tab.insert(j+1, a[i])
                break
    return tab


table = randint(0, 1000, 100)
table = list(table)
table_sorted1 = bubble(table)
table_sorted2 = insertion_sort(table)

print("Numbers before sort:\n", table, "\n")
print("Numbers after bubblesort:\n", table_sorted1, "'\n")

print("Numbers after insertion sort:\n", table_sorted2, "\n")
