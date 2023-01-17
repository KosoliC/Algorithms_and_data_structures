#skończone
class Elements:
    def __init__(self, key, data):
        self.key = key
        self.data = data

class Hash_table:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def hash(self, key):
        if isinstance(key, int):
            modulo = key % self.size
            return modulo
        if isinstance(key, str):
            char = 0
            for i in key:
                char += ord(i)
            modulo = char % self.size
            return modulo


    def solve_coll(self, key , i):
        return ((self.hash(key) + self.c1 * i + self.c2 * i*i) % self.size)

    def search(self, key):
        i = 0
        id = self.hash(key)
        while i < self.size :
            if self.tab[id] is not None and self.tab[id].key == key:
                return self.tab[id].data
            else:
                i += 1
                id = self.solve_coll(key, i)
        return None


    def insert(self, key, data):
        elem = Elements(key,data)
        temp = 0
        id = self.hash(key)

        for i in range(self.size):
            if self.tab[id] is None or self.tab[id].key == key:
                self.tab[id] = elem
                break
            else:
                i += 1
                id = self.solve_coll(key, i)
            temp += 1

        if temp == self.size:
            print("Brak miejsca")


    def remove(self, key):
        i = 0
        id = self.hash(key)

        while True:
            if self.tab[id] is None or self.tab[id].key == key:
                self.tab[id] = None
                break
            else:
                i += 1
                i = self.solve_coll(key, i)
            if i >= self.size:
                print('Brak danej')
                break

    def __str__(self):
        temp = dict()
        for i in self.tab:
            if i is not None:
                temp[i.key] = i.data
            else:
                temp[i] = None
        return str(temp)


def test_1():
    hash_table = Hash_table(13, c1 = 1, c2 = 0)

    data = 'ABCDEFGHIJKLMNO'

    for i in range(len(data)):
        if i + 1 not in [6, 7]:
            hash_table.insert(i + 1, data[i])
        elif i + 1 == 6:
            hash_table.insert(18, data[i])
        elif i + 1 == 7:
            hash_table.insert(31, data[i])

    print(hash_table,'\n')
    print(hash_table.search(5),'\n')
    print(hash_table.search(14),'\n')
    hash_table.insert(5,'Z')
    print(hash_table.search(5),'\n')
    hash_table.remove(5)
    print(hash_table,'\n')
    hash_table.insert('test', 'W')
    print(hash_table.search(31),'\n')
    print(hash_table, '\n')

test_1()

def test_2():
    hash_table = Hash_table(13, c1 = 1, c2 = 0)

    data = 'ABCDEFGHIJKLMNO'

    for i in range(len(data)):
        hash_table.insert(i*13, data[i])

    print(hash_table,'\n')

    hash_table_2 = Hash_table(13, c1 = 0, c2 = 1)

    for i in range(len(data)):
        hash_table_2.insert(i*13, data[i])

    print(hash_table_2,'\n')

    hash_table_3 = Hash_table(13, c1 = 0, c2 = 1)

    for i in range(len(data)):
        if i + 1 not in [6, 7]:
            hash_table_3.insert(i + 1, data[i])
        elif i + 1 == 6:
            hash_table_3.insert(18, data[i])
        elif i + 1 == 7:
            hash_table_3.insert(31, data[i])

    print(hash_table_3,'\n')
test_2()