#nie działa take
class Elements:
    def __init__(self,data):
        self.data = data
        self.next = None

def create():
    return nil()

def nil():
    return Elements(None)

def cons(el, list):
    temp = list
    list = Elements(el)
    list.next = temp
    return list

def first(list):
    return list.data

def get(list):
    return first(list)

def rest(list):
    return list.next

def remove(list):
    if is_empty(list):
        print("List is empty")
    else:
        return rest(list)

def is_empty(list) -> bool:
    if first(list) is None:
        return True
    else:
        return False

def length(list) -> int:
    if is_empty(list):
        return 0
    else:
        return length(rest(list)) + 1

def _print_(list, s=""):
    if is_empty(list):
        print(s[:-1])
    else:
        _print_(rest(list), s + str(first(list)) + '\n')

def add_end(el, list):
    if is_empty(list):
        return cons(el, list)  # dojście do końca i wstawienie tam elementu
    else:
        first_el = first(list)       # podział listy na: pierwszy element
        rest_list = rest(list)      # i całą resztę
        recreated_list = add_end(el, rest_list) # 'zejście 'w dół' rekurencji z przekazaniem dodawanego elementu, przy powrocie 'w górę' zwracana jest odtworzona lista
        return cons(first_el, recreated_list)   # cons dołącza pierwszy element do 'odtwarzanej' przez rekurencję listy

def remove_end(list):
    if length(list) == 1:
        return remove(list)
    else:
        first_el = first(list)
        rest_list = rest(list)
        recreated_list = remove_end(rest_list)
        return cons(first_el,recreated_list)

def take(list, n:int):
    if length(list) > n and n >= 0:
        if n == 1:
            return cons(first(list), create())
        else:
            return cons(first(list), take(rest(list), n - 1))
    else:
        raise ValueError("n is incorrect")

def drop(list, n:int):
    if length(list) > n and n >= 0:
        if n == 0:
            return list
        else:
            return drop(rest(list), n - 1)
    else:
        raise ValueError("n is incorrect")

lista = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]

list = create()
for i in lista:
    list = add_end(i, list)


print('Pełna lista :')
_print_(list)
print("-" * 40)
print('Długość listy: ', length(list))
print("-" * 40)
print('Pierwszy element listy: ', first(list))
list = remove(list)
print("-" * 40)
print('Pierwszy element listy(po uprzednim usunięciu poprzedniego pierwszego elementu): ','\n', first(list))
print("-" * 40)
print("Dodanie na końcu listy dodatkowego elementu:")
_print_(add_end(('KUL', 'Lublin', '1918'),list))
print("-" * 40)
print("Usunięcie elementu na końcu listy:")
remove_end(list)
_print_(list)
print("-" * 40)
print('Lista wiązana złożona z 3 pierwszych elementów listy wiązanej:')
list2 = take(list, 3)
_print_(list2)
print("-" * 40)
print('Lista wiązana złożona z pominięciem 2 pierwszych elementów listy wiązanej:')
list3 = drop(list, 2)
_print_(list3)
print("-" * 40)
print("Czy lista jest pusta? :",is_empty(list))
list = nil()
print("-" * 40)
print("Czy lista jest pusta? :", is_empty(list))
