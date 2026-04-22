import math


class Node:
    """
    Ağaç yapısındaki her bir düğümü temsil eder.
    """

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def find_min_cost_path(root):
    """
    DFS kullanarak kökten yaprağa en düşük maliyetli yolu bulur.
    """
    # Başlangıç değerleri
    best_path = []
    min_total_cost = math.inf

    def dfs(current_node, current_path, current_sum):
        nonlocal min_total_cost, best_path

        # Mevcut düğümü yola ve maliyete ekle
        path_so_far = current_path + [current_node.name]
        total_so_far = current_sum + current_node.cost

        # Eğer bir yaprak düğümse (child yoksa) kontrol et
        if not current_node.children:
            if total_so_far < min_total_cost:
                min_total_cost = total_so_far
                best_path = path_so_far
            return

        # Çocuk düğümler için derinleş
        for child in current_node.children:
            dfs(child, path_so_far, total_so_far)

    # Aramayı başlat
    dfs(root, [], 0)
    return best_path, min_total_cost


# --- Örnek Ağaç Oluşturma ---
#        A(5)
#       /    \
#     B(10)   C(2)
#    /    \     \
# D(1)    E(20)  F(4)

root = Node("A", 5)
node_b = Node("B", 10)
node_c = Node("C", 2)
node_d = Node("D", 1)
node_e = Node("E", 20)
node_f = Node("F", 4)

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)

# --- Çözüm ---
path, cost = find_min_cost_path(root)

print(f"En Küçük Maliyetli Dal: {' -> '.join(path)}")
print(f"Toplam Maliyet: {cost}")

# Doğrulama:
# A-B-D: 5+10+1 = 16
# A-B-E: 5+10+20 = 35
# A-C-F: 5+2+4 = 11 (En küçük)