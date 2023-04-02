from src.bplustree import bplus_tree
from tabulate import tabulate

tree = bplus_tree()
tree.open("./")

for i in range(1, 10000):
    tree.insert(i, i+1)

for i in range(6000, 7000):
    print(tree.get(i))

