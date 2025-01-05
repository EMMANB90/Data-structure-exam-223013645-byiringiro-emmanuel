class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def display(self, node, level=0):
        print(" " * level * 2 + str(node.data))
        for child in node.children:
            self.display(child, level + 1)

# Example usage
booking_tree = Tree("Root")

# Adding branches to the root (e.g., different service categories)
service_1 = TreeNode("Emergency Services")
service_2 = TreeNode("Regular Maintenance")
booking_tree.root.add_child(service_1)
booking_tree.root.add_child(service_2)

# Adding sub-branches (e.g., specific types of services)
service_1.add_child(TreeNode("Pipe Burst Repair"))
service_1.add_child(TreeNode("Drain Cleaning Services"))
service_2.add_child(TreeNode("Leak Detection"))
service_2.add_child(TreeNode("Water Heater Maintenance"))

# Displaying the hierarchy
print("Hierarchical Structure of Services:")
booking_tree.display(booking_tree.root)

