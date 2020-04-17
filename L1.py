import numpy as np
import time


def bubble(a):
    tab_size = np.size(a)
    tab = a.copy()
    ind = list(range(tab_size))
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

                in1 = ind[i]
                in2 = ind[i + 1]
                ind[i] = in2
                ind[i + 1] = in1
    return tab, ind


def insertion_sort(a):
    tab_size = np.size(a)
    tab = [a[0]]
    ind = [0]
    for i in range(1, tab_size):
        for j in range(tab_size):
            if a[i] < tab[j]:
                tab.insert(j, a[i])
                ind.insert(j, i)
                break
            elif j == (np.size(tab)-1):
                tab.insert(j+1, a[i])
                ind.insert(j+1, i)
                break
    return tab, ind


def bigger_than_b_bubble(a, b):
    tab_size = np.size(a)
    a, ind = bubble(a)
    ret = []
    for i in range(tab_size):
        if i < tab_size-3 and a[i] > b:
            ret.append(ind[i+2])
            ret.append(ind[i+1])
            ret.append(ind[i])
            break
    return ret


def bigger_than_b_insertion(a, b):
    tab_size = np.size(a)
    a, ind = insertion_sort(a)
    ret = []
    for i in range(tab_size):
        if i < tab_size-3 and a[i] > b:
            ret.append(ind[i+2])
            ret.append(ind[i+1])
            ret.append(ind[i])
            break
    return ret


def create_data_sets(number_of_sets):
    data_sets = []
    for i in range(number_of_sets):
        data_sets.append(list(np.random.random(100*(i+1))*100))
    return data_sets


number_of_data_sets = 5
dane = create_data_sets(number_of_data_sets)
times_bubble = []
times_insertion = []
table1 = []
table2 = []

for k in range(number_of_data_sets):

    start_time_insertion = time.time()
    table2.append(bigger_than_b_insertion(dane[k], 20))
    end_time_insertion = time.time()
    times_insertion.append(end_time_insertion - start_time_insertion)

    start_time_bubble = time.time()
    table1.append(bigger_than_b_bubble(dane[k], 20))
    end_time_bubble = time.time()
    times_bubble.append(end_time_bubble - start_time_bubble)


print(table1)
print(times_bubble)

print(table2)
print(times_insertion)
