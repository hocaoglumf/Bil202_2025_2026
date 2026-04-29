class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """Hiyerarşide kaçıncı seviyede olduğunu hesaplar."""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        """Ağacı görsel olarak yazdırır."""
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    # Kök dizin (Root)
    root = TreeNode("Elektronik")

    # Alt dallar (Sub-trees)
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Asus"))

    phone = TreeNode("Cep Telefonu")
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Samsung"))

    tv = TreeNode("Televizyon")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    # Dalları köke bağlama
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()


