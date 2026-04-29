class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.children = []


def find_min_cost_path(node):
    # Eğer düğüm bir yaprak (leaf) ise, sadece kendi maliyetini ve ismini döner
    if not node.children:
        return node.cost, [node.name]

    min_total_cost = float('inf')
    best_path = []

    # Çocuklar arasında en düşük maliyetli yolu ara
    for child in node.children:
        child_cost, child_path = find_min_cost_path(child)

        if child_cost < min_total_cost:
            min_total_cost = child_cost
            best_path = child_path

    # Mevcut düğümün maliyetini alt yoldan gelen maliyete ekle
    return node.cost + min_total_cost, [node.name] + best_path


# --- Ağaç Yapısını Kuralım ---
# Kök: Market (Maliyet: 10)
root = Node("Market", 10)

# 1. Dal: Lojistik A (Maliyet: 5) -> Depo 1 (Maliyet: 2)
branch_a = Node("Lojistik A", 5)
branch_a.children.append(Node("Depo 1", 2))

# 2. Dal: Lojistik B (Maliyet: 2) -> Depo 2 (Maliyet: 8)
branch_b = Node("Lojistik B", 2)
branch_b.children.append(Node("Depo 2", 8))

root.children.extend([branch_a, branch_b])

# --- Hesaplama ---
total_cost, path = find_min_cost_path(root)

print(f"En Düşük Maliyet: {total_cost}")
print(f"İzlenen Yol: {' -> '.join(path)}")