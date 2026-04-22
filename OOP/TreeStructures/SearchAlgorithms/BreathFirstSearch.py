class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def bfs_list_simple(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)  # ilk elemanı al
        print(node.value)

        for child in node.children:
            queue.append(child)


# Örnek ağaç oluşturalım
'''
              A
        B          C
    D       E      F
'''

# Örnek
root = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

root.children = [b, c]
b.children = [d, e]
c.children = [f]

bfs_list_simple(root)