#skończone

def realloc(tab, size: int):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]

class Queue:
    def __init__(self):
        self.tab = [ None for i in range(5) ]  # tworze pustą tablice o rozmiarze 5
        self.size = 5     # rozmiar tablicy
        self.save_id = 0  # miejsce zapisu danych
        self.read_id = 0  # miejsce odczytu danych

    def is_empty(self) -> bool:
        if self.save_id == self.read_id:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.tab[self.read_id]
        else:
            return None

    def dequeue(self):
        if not self.is_empty():
            temp = self.read_id
            self.read_id += 1
            if self.read_id >= self.size:
                self.read_id = 0
            return self.tab[temp]
        else:
            return None

    def enqueue(self, data):
        self.tab[self.save_id] = data[0]
        self.save_id += 1
        for k in range(len(data)-1):
            if self.save_id >= self.size:
                self.save_id = 0
            if self.save_id == self.read_id:
                self.tab = realloc(self.tab, self.size*2)
                for i in range(self.size):
                    self.tab[(2*self.size)- 1 - i] = self.tab[self.size - 1 - i]
                for j in range(self.size):
                    self.tab[self.save_id + j] = None
                self.read_id += self.size
                self.size *= 2
                self.tab[self.save_id] = data[k+1]
                self.save_id += 1
            else:
                self.tab[self.save_id] = data[k+1]
                self.save_id += 1

    def print_tab(self):
        print(self.tab)


    def print_queue(self):
        temp_start = self.read_id
        temp_end = self.save_id
        print('[', end=' ')
        if not self.is_empty():
            if temp_end <= temp_start:
                temp_end += self.size
            for i in range(temp_end - temp_start):
                if temp_start + i >= self.size:
                    print(self.tab[temp_start + i - self.size], end=', ')
                else:
                    print(self.tab[temp_start + i], end=', ')
        print(']')


def main():
    queue = Queue()
    queue.enqueue([1, 2, 3, 4])
    print(queue.dequeue())
    print(queue.peek())
    queue.print_queue()
    queue.enqueue([5, 6, 7, 8])
    queue.print_tab()

    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_queue()
main()