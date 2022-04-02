class Elements:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:

    def __init__(self):
        self.root = None

    def search(self, key):
        if self.root is None:
            raise ValueError("Tree is empty")

        else:
            node = self.root
            while node:
                if node.key > key:
                    node = node.left_child

                if node.key < key:
                    node = node.right_child

                else:
                    return node.value


    def insert(self, key, value):
        if self.root is None:
            self.root = Elements(key, value)
        else:
            self.root = self.insert_(key, value, self.root)


    def insert_(self, key, value, node):
        if node is None:
            return Elements(key, value)
        if key < node.key:
            node.left_child = self.insert_(key, value, node.left_child)
            return node
        elif key > node.key:
            node.right_child = self.insert_(key, value, node.right_child)
            return node
        else:
            node.value = value
            return node

    def delete(self, key, node = None):
        if node is None:
            node = self.root
        if node:
            if key < node.key:
                node.left_child = self.delete(key, node.left_child)
                return node
            elif key > node.key:
                node.right_child = self.delete(key, node.right_child)
                return node
            else:
                if not node.left_child and not node.right_child: # węzeł bez potomków
                    return None

                if not node.left_child and node.right_child: # węzeł z jednym potomkiem
                    return node.right_child

                if node.left_child and not node.right_child: # węzeł z jednym potomkiem
                    return node.left_child

                else: #węzeł z dwoma potomkami
                    parent = node.right_child

                    if parent.left_child is not None:
                        child = parent.left_child
                    else:
                        parent.left_child = node.left_child
                        return parent

                    while child.left_child:
                        parent = child
                        child = child.left_child

                    node.value = child.value
                    node.key = child.key

                    if child.right_child is not None:
                        parent.left_child = child.right_child

                    else:
                        parent.left_child = None

                    return node

        else:
            raise ValueError("Tree is empty")

    def _print_(self, tree_elements = [], node = None):

        if node is None:
            node = self.root

        if node.left_child is not None:
            self._print_(tree_elements, node.left_child)

        tree_elements.append(str(node.key) +":"+ str(node.value))
        if node.right_child is not None:
            self._print_(tree_elements, node.right_child)

        return tree_elements

    def print_(self):
        tree_elements = []
        temp = self._print_(tree_elements)
        print(temp)

    def height(self,  node = None , h = 0):
        if node is None:
            node = self.root
        height = [1]

        if node.left_child is not None:
            height.append(self.height(node.left_child, h + 1))

        if node.right_child is not None:
            height.append(self.height(node.right_child, h + 1))

        if node.left_child is None and node.right_child is None:
            height.append(h)

        if any(height):
            return max(height)

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node != None:
            self._print_tree(node.right_child, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left_child, lvl + 5)

def main():

    BST_tree = BST()
    nodes = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}

    for i,j in nodes.items():
        BST_tree.insert(i,j)

    BST_tree.print_tree()
    BST_tree.print_()
    print(BST_tree.search(24))
    BST_tree.insert(20, 'AA')
    BST_tree.insert(6, 'M')
    BST_tree.delete(62)
    BST_tree.insert(59, 'N')
    BST_tree.insert(100, 'P')
    BST_tree.delete(8)
    BST_tree.delete(15)
    BST_tree.insert(55, 'R')
    BST_tree.delete(50)
    BST_tree.delete(5)
    BST_tree.delete(24)
    print(BST_tree.height())
    BST_tree.print_()
    BST_tree.print_tree()


main()