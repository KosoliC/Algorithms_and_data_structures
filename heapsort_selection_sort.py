import random
from functools import wraps
from timeit import default_timer as timer
import copy

class Element:
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority


    def __lt__(self, other):  # metoda magiczna pozwalająca użyć operatora <
        return self.priority < other.priority


    def __ge__(self, other): # metoda magiczna pozwalająca użyć operatora >=
        return self.priority >= other.priority


    def __str__(self):
        return str(self.priority)+':'+str(self.data)


class Queue:
    def __init__(self, tab_sort=None):
        if tab_sort:
            temp_tab = []
            for i in tab_sort:
                if isinstance(i, tuple):
                    temp_tab.append(Element(i[0],i[1]))
                else:
                    temp_tab.append(Element(i,0))
            self.tab = temp_tab
            self.size = len(self.tab)

            self.heapify()
        else:
            self.tab = []
            self.size = len(self.tab)


    def is_empty(self):
        if not self.tab:
            return True
        else:
            return False

    def peek(self):
        return self.tab[0].data

    def dequeue(self):
        if self.is_empty():
            return None

        elif self.size == 1:
            return self.tab[0]

        else:  # zwracam daną o najwyższym priorytecie (zdejmując ją z wierzchołka kopca)
            self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
            self.size -= 1
            i = 0
            self.repair(i)

    def repair(self, parent=0):
        temp = self.tab[0]

        while self.right(parent) < self.size:

            if self.tab[self.left(parent)] < self.tab[self.right(parent)]:
                if self.tab[parent] < self.tab[self.right(parent)]:
                    self.tab[self.right(parent)], self.tab[parent] = self.tab[parent], self.tab[self.right(parent)]
                    parent = self.right(parent)
                elif self.tab[parent] < self.tab[self.left(parent)]:
                    self.tab[self.left(parent)], self.tab[parent] = self.tab[parent], self.tab[self.left(parent)]
                    parent = self.left(parent)
                else:
                    break

            else:
                if self.tab[parent] < self.tab[self.left(parent)]:
                    self.tab[self.left(parent)], self.tab[parent] = self.tab[parent], self.tab[self.left(parent)]
                    parent = self.left(parent)
                elif self.tab[parent] < self.tab[self.right(parent)]:
                    self.tab[self.right(parent)], self.tab[parent] = self.tab[parent], self.tab[self.right(parent)]
                    parent = self.right(parent)
                else:
                    break

        if self.left(parent) < self.size and self.tab[self.left(parent)] > self.tab[parent]:
            self.tab[self.left(parent)], self.tab[parent] = self.tab[parent], self.tab[self.left(parent)]

        return temp.data


    def heapify(self):
        for i in range(self.size//2 - 1 ,-1, -1):
            self.repair(i)


    def enqueue(self, priority, data):
        new_elem = Element(priority, data)

        if not self.tab:
            self.tab.append(new_elem)
            self.size += 1
        else:
            self.tab.append(new_elem)
            self.size += 1
            parent = self.parent(self.size-1)
            child = self.size - 1
            while True:
                if child == 0:
                    break
                if self.tab[self.size-1] >= self.tab[parent]:

                    self.tab[child], self.tab[parent] = self.tab[parent], self.tab[child]
                    child = parent

                else:
                    break

    def left(self, parent_index):
        left_child = 2*parent_index + 1
        return left_child

    def right(self, parent_index):
        right_child = 2*parent_index + 2
        return right_child

    def parent(self, index):
        parent = (index-1)//2
        return parent

    def print_tab(self):
        print('{', end=' ')
        if len(self.tab) > 0:
            for i in range(len(self.tab) - 1):
                print(self.tab[i] , end=', ')
            if self.tab[len(self.tab) - 1]: print(self.tab[len(self.tab) - 1], end=' ')
        print('}')


    def print_tree(self, idx, lvl):
        if idx < len(self.tab):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def print_tree(tab, idx, lvl):
    if idx < len(tab):
        print_tree(tab, 2 * idx + 2, lvl + 1)
        print(2 * lvl * '  ', tab[idx] if tab[idx] else None)
        print_tree(tab, 2 * idx + 1, lvl + 1)


def swap_sort(list):
    copy_list = copy.deepcopy(list)
    n = len(copy_list)
    for i in range(n):
        min_el = i
        for j in range(i, n):
            if copy_list[j] < copy_list[min_el]:
                min_el = j

                copy_list[i], copy_list[min_el] = copy_list[min_el], copy_list[i]

    return copy_list


def shift_sort(list):
    copy_list = copy.deepcopy(list)
    n = len(copy_list)
    i = 1
    while i < n:
        j = i
        while j > 0 and copy_list[j - 1] > copy_list[j]:
            copy_list[j], copy_list[j - 1] = copy_list[j - 1], copy_list[j]
            j -= 1
        i += 1

    return copy_list


def test1():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    print(tab, '\n')
    print_tree(tab, 0 ,0)
    print('\n')
    tab_to_sort = Queue(tab)
    tab_to_sort.print_tree(0,0)
    tab_to_sort.print_tab()
    while tab_to_sort.size > 1:
        tab_to_sort.dequeue()
    tab_to_sort.print_tab()

test1()

def test2():
    rand_tab = [random.randint(0, 99) for _ in range(10000)]
    # print(rand_tab, '\n')
    # print_tree(rand_tab, 0, 0)
    print('\n')
    t_start = timer()
    rand_tab_to_sort = Queue(rand_tab)
    while rand_tab_to_sort.size > 1:
        rand_tab_to_sort.dequeue()
    t_stop = timer()
    # tab_to_sort.print_tree(0, 0)
    # tab_to_sort.print_tab()
    print("Czas obliczeń dla kopcowego :", "{:.7f}".format(t_stop - t_start),'\n')

test2()

def test_3():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    swapped = swap_sort(tab)
    shifted = shift_sort(tab)
    print('Swapped: ',swapped)
    print('Shifted: ',shifted)

test_3()

def test_4():
    rand_tab = [random.randint(0, 99) for _ in range(10000)]
    t_start_swap = timer()
    swap_sort(rand_tab)
    t_stop_swap = timer()

    t_start_shift= timer()
    shift_sort(rand_tab)
    t_stop_shift = timer()

    print("Czas obliczeń dla swap:", "{:.7f}".format(t_stop_swap - t_start_swap))
    print("Czas obliczeń dla shift:", "{:.7f}".format(t_stop_shift - t_start_shift))

test_4()