import numpy as np
import time
import string


def string_compare(P: str, T: str, i: int, j: int):
    if i == 0:
        return j - 1
    if j == 0:
        return i - 1

    swap = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    insert = string_compare(P, T, i, j - 1) + 1
    delete = string_compare(P, T, i - 1, j) + 1

    lowest_cost = min(swap, insert, delete)

    return lowest_cost

def string_compare_pd(P: str, T: str):
    i = len(P) - 1
    j = len(T) - 1

    D = np.zeros((len(P), len(T)))
    for k in range(0, i + 1):
        D[[k], 0] = k
    for l in range(0, j + 1):
        D[0, [l]] = l

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]

    parents[0][1:] = ['I' for _ in range(1, len(T))]
    for _ in range(1, len(P)):
        parents[_][0] = 'D'

    parents[0][0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            match = (D[i - 1][j - 1] + (P[i] != T[j]), 'S')
            insert = (D[i][j - 1] + 1, 'I')
            delete = (D[i - 1][j] + 1, 'D')
            lowest_cost = min([match, insert, delete], key=lambda k: k[0])

            D[i][j] = lowest_cost[0]

            if lowest_cost[1] == 'S' and P[i] == T[j]:
                parents[i][j] = 'M'
            else:
                parents[i][j] = lowest_cost[1]

    cost = D[-1][-1]
    return int(cost),parents

def find_path(parents, i,j,path):
    idx = parents[i][j]
    if idx == 'X':
        return path
    if idx == 'M':
        find_path(parents,i - 1, j - 1, path)
        path.append('M')

    if idx == 'S':
        find_path(parents,i - 1, j - 1, path)
        path.append('S')

    if idx == 'I':
        find_path(parents, i, j - 1, path)
        path.append('I')

    if idx == 'D':
        find_path(parents, i - 1, j, path)
        path.append('D')

    return ''.join(path)

def fitting(P,T,idx = 'end'):
    D = np.zeros((len(P), len(T)))
    for k in range(0, len(P)):
        D[[k], 0] = k

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            match = (D[i - 1][j - 1] + (P[i] != T[j]), 'S')
            insert = (D[i][j - 1] + 1, 'I')
            delete = (D[i - 1][j] + 1, 'D')
            lowest_cost = min([match, insert, delete], key=lambda k: k[0])

            D[i][j] = lowest_cost[0]
    last_row = len(P) - 1
    min_el = np.argmin(D[last_row,:])

    if idx == 'end':
        return min_el
    elif idx == 'start':
        length = 0
        for i in P:
            length += 1 if i not in string.whitespace else 0

        return min_el - length + 1

def longest_seq(P: str, T: str):
    multiplier = 1000000
    i = len(P) - 1
    j = len(T) - 1

    D = np.zeros((len(P), len(T)))
    for k in range(0, i + 1):
        D[[k], 0] = k
    for l in range(0, j + 1):
        D[0, [l]] = l

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]

    parents[0][1:] = ['I' for _ in range(1, len(T))]
    for _ in range(1, len(P)):
        parents[_][0] = 'D'

    parents[0][0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            match = (D[i - 1][j - 1] + (P[i] != T[j])*multiplier, 'S')
            insert = (D[i][j - 1] + 1, 'I')
            delete = (D[i - 1][j] + 1, 'D')
            lowest_cost = min([match, insert, delete], key=lambda k: k[0])

            D[i][j] = lowest_cost[0]

            if lowest_cost[1] == 'S' and P[i] == T[j]:
                parents[i][j] = 'M'
            else:
                parents[i][j] = lowest_cost[1]


    path = find_path(parents, len(P) - 1, len(T) - 1, [])
    seq = ''
    deleted = 0
    for i in range(len(path)):
        if path[i] == 'M':
            seq += T[i - deleted + 1]
        if path[i] == 'D':
            deleted += 1

    return seq

def longest_seq_mono(T: str):
    P = ''.join(sorted(T))
    result = longest_seq(P,T)
    return result

def main():
    P = ' kot'
    T = ' pies'

    cost = string_compare(P, T, len(P) - 1, len(T) - 1)
    print(cost)

    P3 = ' biały autobus'
    T3 = ' czarny autokar'

    cost_pd = string_compare_pd(P3, T3)
    print(cost_pd[0])

    P_path = ' thou shalt not'
    T_path = ' you should not'
    parents_path = string_compare_pd(P_path, T_path)
    path = find_path(parents_path[1],len(P_path)-1, len(T_path)-1,[])
    print(path)

    P_fit = ' ban'
    T_fit = ' mokeyssbanana'

    idx = fitting(P_fit, T_fit, 'start')
    print(idx)

    P_longest = ' democrat'
    T_longest = ' republican'

    longest_word = longest_seq(P_longest,T_longest)
    print(longest_word)

    T_longest_mon = ' 243517698'
    longest_word_mon = longest_seq_mono(T_longest_mon)
    print(longest_word_mon)
main()