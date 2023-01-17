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
    def __init__(self):
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

        temp = self.tab[0]

        if len(self.tab) == 1:
            self.tab.pop()
            return temp.data

        else:  # zwracam daną o najwyższym priorytecie (zdejmując ją z wierzchołka kopca)
            self.tab[0] = self.tab.pop()

            parent = 0
            while self.right(parent) < len(self.tab):

                if self.tab[self.left(parent)] < self.tab[self.right(parent)]:
                    if self.tab[parent] < self.tab[self.right(parent)]:
                        self.tab[self.right(parent)], self.tab[parent] = self.tab[parent], self.tab[self.right(parent)]
                        parent = self.right(parent)
                    elif self.tab[parent] < self.tab[self.left(parent)]:
                        self.tab[self.left(parent)], self.tab[parent] = self.tab[parent], self.tab[self.left(parent)]
                        parent = self.left(parent)

                else:
                    if self.tab[parent] < self.tab[self.left(parent)]:
                        self.tab[self.left(parent)], self.tab[parent] = self.tab[parent], self.tab[self.left(parent)]
                        parent = self.left(parent)
                    elif self.tab[parent] < self.tab[self.right(parent)]:
                        self.tab[self.right(parent)], self.tab[parent] = self.tab[parent], self.tab[self.right(parent)]
                        parent = self.right(parent)

            if self.left(parent) < len(self.tab) and self.tab[self.left(parent)] > self.tab[parent]:
                self.tab[self.left(parent)], self.tab[parent] = self.tab[parent], self.tab[self.left(parent)]

            return temp.data

    def enqueue(self, priority, data):
        new_elem = Element(priority, data)

        if not self.tab:
            self.tab.append(new_elem)
        else:
            self.tab.append(new_elem)
            parent = self.parent(len(self.tab)-1)
            child = len(self.tab)-1
            while True:
                if child == 0:
                    break
                if self.tab[len(self.tab)-1] >= self.tab[parent]:

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

def main():
    queue = Queue()

    for i,j in zip([4,7,6,7,5,2,2,1],"ALGORYTM"):
        queue.enqueue(i, j)

    queue.print_tree(0, 0)
    queue.print_tab()
    print(queue.dequeue())
    print(queue.peek())
    queue.print_tab()
    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_tab()

main()