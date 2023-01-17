from timeit import default_timer as timer
import time

def naive_method(S, W):
    counter = 0
    founded = []
    m = 0

    while m <= (len(S) - len(W)):
        j = 0
        while j < len(W):
            counter += 1
            if S[m + j] != W[j]:
                break
            j += 1

        if j == len(W):
            founded.append(m)
        m += 1

    return len(founded),counter

def hash(word, N):
    d = 256
    q = 101
    # hw = (ord(word[0]) * d) % q
    hw = 0
    for i in range(N):
        hw = (hw * d + ord(word[i])) % q
    return hw

def RabinKarp(S, W):
    counter = 0
    founded = []
    colision = 0
    d = 256
    q = 101
    h = 1
    for i in range(len(W) -1):
        h = (h * d) % q

    hW = hash(W,len(W))
    hS = hash(S[:len(W)], len(W))
    for m in range(0, len(S)-len(W) + 1):
        counter += 1
        if hS == hW:
            if S[m:(m+len(W))] == W:
                founded.append(m)
            else:
                colision += 1
        if m + len(W) < len(S):
            hS = (d*(hS - ord(S[m])*h)+ ord(S[m + len(W)])) % q

    return len(founded),counter, colision

def kmp_table(W):
    T = [0 for _ in range(len(W)+1)]
    pos = 1
    cnd = 0
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T

def kmp_search(S,W):
    founded = []
    counter = 0
    m = 0
    i = 0
    T = kmp_table(W)
    nP = 0
    while m < len(S):
        counter += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                founded.append(m - i)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    return len(founded), counter


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()

    print("Metoda naiwna")
    t_start = time.perf_counter()
    founded, counter = naive_method(S, "time.")
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(founded,';', counter,'\n')

    print("Metoda Rabina-Karpa")
    t_start = time.perf_counter()
    founded, counter, colision = RabinKarp(S, "time.")
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(founded,';', counter,';',colision,'\n')

    print("Metoda Knuth-Morris-Pratta")
    t_start = time.perf_counter()
    founded, counter = kmp_search(S, "time.")
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(founded,';', counter)

main()


