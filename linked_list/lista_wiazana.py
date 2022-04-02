#skończone
from __future__ import annotations

class Elements:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, element):
        new_element = Elements(element)

        if self.head is None:
            self.head = new_element

        else:
            self.head, new_element.next = new_element, self.head

    def remove(self):
        if self.head is None:
            print("List is empty")

        else:
            move = self.head.next
            self.head = move

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def length(self) -> int:
        length = 0
        len_copy = self.head

        if self.is_empty():
            return 0
        else:
            while len_copy:
                len_copy = len_copy.next
                length += 1
            return length

    def get(self) -> Elements.data:
        if not self.is_empty():
            return self.head.data
        else:
            raise ValueError("List is empty")

    def print(self):
        print_list = self.head

        if self.head is None:
            print("List is empty")
        else:
            while print_list:
                print("{}".format(print_list.data))
                print_list = print_list.next


    def add_back(self, new_element):
        last_element = Elements(new_element)

        if self.is_empty():
            self.head = last_element
        else:
            head_rekursive = self.head

            while head_rekursive.next:
                head_rekursive = head_rekursive.next

            head_rekursive.next = last_element

    def remove_back(self):

        if self.is_empty():
            raise ValueError("List is empty")
        else:
            head_rekursive = self.head

            while head_rekursive.next.next:
                head_rekursive = head_rekursive.next

            head_rekursive.next = None

    def take(self, n: int):
        count = 0

        linkedlst = Linked_list()
        node = self.head
        reverselst = Linked_list()

        linkedlst.add(node.data)
        while count < self.length() and count < n:
            linkedlst.add(node.data)
            node = node.next
            count += 1

        node_copy = linkedlst.head
        for j in range(count):
            reverselst.add(node_copy.data)
            node_copy = node_copy.next
        return reverselst

    def drop(self, n:int):
        count = 0
        linkedlst = Linked_list()
        emptylist = Linked_list()
        node = self.head

        if n >= self.length():
            return emptylist
        else:
            while count < self.length():
                if count <= (n-1):
                    node = node.next
                    count += 1
                if count > n-1:
                    linkedlst.add_back(node.data)
                    node = node.next
                    count += 1

            return linkedlst

def main():

    lista = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]

    Lnkd_lst = Linked_list()

    for i in lista:
        Lnkd_lst.add_back(i)

    print('Pełna lista wiązana:')
    Lnkd_lst.print()
    print("-" * 40)
    print('Długość listy: ', Lnkd_lst.length())
    print("-" * 40)
    print('Pierwszy element listy: ', Lnkd_lst.get())
    Lnkd_lst.remove()
    print("-" * 40)
    print('Pierwszy element listy(po uprzednim usunięciu poprzedniego pierwszego elementu): ','\n', Lnkd_lst.get())
    print("-" * 40)
    print("Dodanie na końcu listy dodatkowego elementu:")
    Lnkd_lst.add_back(('KUL', 'Lublin', '1918'))
    Lnkd_lst.print()
    print("-" * 40)
    print("Usunięcie elementu na końcu listy:")
    Lnkd_lst.remove_back()
    Lnkd_lst.print()
    print("-" * 40)
    print('Lista wiązana złożona z 2 pierwszych elementów listy wiązanej:')
    new_list = Lnkd_lst.take(2)
    new_list.print()
    print("-" * 40)
    print('Lista wiązana złożona z pominięciem 3 pierwszych elementów listy wiązanej:')
    new_list2 = Lnkd_lst.drop(3)
    new_list2.print()
    print("-" * 40)
    print("Czy lista jest pusta? :",Lnkd_lst.is_empty())
    Lnkd_lst.destroy()
    print("-" * 40)
    print("Czy lista jest pusta? :", Lnkd_lst.is_empty())

main()
