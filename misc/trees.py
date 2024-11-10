class BinaryTree:
    class TreeNode:
        def __init__(self, value=None):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, binary_string=None):
        self.root = None
        if binary_string is not None:
            self.root = self.build_tree(binary_string)

    def build_tree(self, binary_string):
        """Builds a binary tree from the binary string for reconstructing the string via pre-order traversal."""
        if not binary_string:
            return None

        root = self.TreeNode(binary_string[0])
        mid = len(binary_string) >> 1
        root.left = self.build_tree(binary_string[1:mid+1])
        root.right = self.build_tree(binary_string[mid+1:])

        return root

    def preorder_traversal(self, root=None):
        """Returns the binary string reconstructed via pre-order traversal."""
        if root is None:
            root = self.root
        result = root.value
        if root.left:
            result += self.preorder_traversal(root.left)
        if root.right:
            result += self.preorder_traversal(root.right)
        return result

    def postorder_traversal(self, root=None):
        """Returns the binary string reconstructed via post-order traversal."""
        if root is None:
            root = self.root
        result = ""
        if root.right:
            result += self.postorder_traversal(root.right)
        if root.left:
            result += self.postorder_traversal(root.left)
        #if root.right:
        #    result += self.postorder_traversal(root.right)
        result += root.value
        return result

    def print_tree(self, root=None, level=0, prefix="Root: "):
        """Prints the binary tree in ASCII format."""
        if root is None:
            root = self.root
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left or root.right:
            if root.left:
                self.print_tree(root.left, level + 1, "L--- ")
            if root.right:
                self.print_tree(root.right, level + 1, "R--- ")

    def count_leaf_nodes(self, root=None):
        """Counts the number of leaf nodes in the binary tree."""
        if root is None:
            root = self.root
        if root.left is None and root.right is None:
            return 1
        return (self.count_leaf_nodes(root.left) if root.left else 0) + \
               (self.count_leaf_nodes(root.right) if root.right else 0)

    def longest_leaf_to_leaf_path(self, root=None):
        """Calculates the longest path between any two leaf nodes in the tree."""
        def helper(node):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return 0

            left_height = helper(node.left)
            right_height = helper(node.right)

            if node.left and node.right:
                self.max_leaf_to_leaf_path = max(self.max_leaf_to_leaf_path, left_height + right_height + 2)

            return max(left_height, right_height) + 1

        self.max_leaf_to_leaf_path = 0
        helper(self.root)
        return self.max_leaf_to_leaf_path


def g(n):
    binary_tree = BinaryTree()
    print("=" * 30)
    binary_string = bin(n)[2:]

    # Build the binary tree
    binary_tree.root = binary_tree.build_tree(binary_string)

    # Perform pre-order traversal and print the reconstructed binary string
    reconstructed_string_preorder = binary_tree.preorder_traversal()
    print(f"Input binary string: {binary_string} (Length: {len(binary_string)})")
    print("Reconstructed string (pre-order):", reconstructed_string_preorder)

    # Perform post-order traversal and print the reconstructed binary string
    reconstructed_string_postorder = binary_tree.postorder_traversal()
    print("Reconstructed string (post-order):", reconstructed_string_postorder)

    # Print the tree structure
    binary_tree.print_tree()

    # Count the leaf nodes and print the result
    leaf_count = binary_tree.count_leaf_nodes()
    print(f"Leaf nodes count: {leaf_count}")

    # Calculate and print the longest leaf-to-leaf path length
    critical_path_length = binary_tree.longest_leaf_to_leaf_path()
    print(f"Critical leaf-to-leaf path length (edges): {critical_path_length}\n")


# Example usage for numbers 1 to 12 and 127 to 138
for n in range(1, 13):
    g(n)

for n in range(127, 139):
    g(n)