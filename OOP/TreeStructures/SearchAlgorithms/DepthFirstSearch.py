class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs_recursive(node):
    if node is None:
        return

    print(node.value)  # düğümü ziyaret et

    for child in node.children:
        dfs_recursive(child)


# Örnek ağaç oluşturalım
'''
              A
        B          C
    D       E      F
'''


root = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

root.children = [b, c]
b.children = [d, e]
c.children = [f]

# DFS çalıştır
dfs_recursive(root)