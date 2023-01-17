import copy
import random
from timeit import default_timer as timer

def swap_sort(list):
    copy_list = copy.deepcopy(list)
    n = len(copy_list)
    for i in range(n - 1):
        min_el = i
        for j in range(i + 1, n):
            if copy_list[j] > copy_list[min_el]:
                min_el = j

                copy_list[i], copy_list[min_el] = copy_list[min_el], copy_list[i]

    return copy_list


def shift_sort(list):
    copy_list = copy.deepcopy(list)
    n = len(copy_list)
    i = 1
    while i < n:
        j = i
        while j > 0 and copy_list[j - 1] < copy_list[j]:
            copy_list[j], copy_list[j - 1] = copy_list[j - 1], copy_list[j]
            j -= 1
        i += 1

    return copy_list

def test_1():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    swapped = swap_sort(tab)
    shifted = shift_sort(tab)
    print(swapped)
    print(shifted)

test_1()

def test_2():
    rand_tab = [random.randint(0, 99) for _ in range(10000)]
    t_start_swap = timer()
    swap_sort(rand_tab)
    t_stop_swap = timer()

    t_start_shift= timer()
    shift_sort(rand_tab)
    t_stop_shift = timer()

    print("Czas obliczeń dla swap:", "{:.7f}".format(t_stop_swap - t_start_swap))
    print("Czas obliczeń dla shift:", "{:.7f}".format(t_stop_shift - t_start_shift))

test_2()



def repair(self, idx=0):
    idx_parent = idx
    while True:
        idx_left_child = self.left(idx_parent)
        idx_right_child = self.right(idx_parent)
        if idx_right_child < self.size and idx_left_child < self.size and \
                self.tab[idx_parent] < self.tab[idx_left_child] < self.tab[idx_right_child]:
            self.tab[idx_parent], self.tab[idx_right_child] = self.tab[idx_right_child], self.tab[idx_parent]
            idx_parent = idx_right_child
        elif idx_left_child < self.size and self.tab[idx_left_child] > self.tab[idx_parent]:
            self.tab[idx_parent], self.tab[idx_left_child] = self.tab[idx_left_child], self.tab[idx_parent]
            idx_parent = idx_left_child
        elif idx_right_child < self.size and self.tab[idx_right_child] > self.tab[idx_parent]:
            self.tab[idx_parent], self.tab[idx_right_child] = self.tab[idx_right_child], self.tab[idx_parent]
            idx_parent = idx_right_child
        else:
            break
