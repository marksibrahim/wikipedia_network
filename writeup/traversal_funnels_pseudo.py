"""
Pseudo Code for Traversal Funnels
"""

Traversal Funnels Algorithm

// 1. Determine Cycles 
for node in Graph
# O(n)
    next_node = node.link
    visited = {node, next_node}
    // advance to potential cycle
    while next_node not in visited:
        # O(path length)
        next_node = next_node.link
        visited.add(next_node)
    // mark cycle
    if (node == next_node):
        node.in_cycle = True

// 2. Compute Traversal Funnels
for node in Graph:
# O(n)
    while node.in_cycle == False:
        # O(path length)
        node.funnels += 1
        node = node.link
