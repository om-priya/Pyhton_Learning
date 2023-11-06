from node import Node
from binary_trees import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

tree.inorder()
# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)