'''
class Node:
    def __init__(self,key):
        self.key = key
        self.neighbors = []
    def add_neighbor(self, othernode):
        self.neighbors.append(othernode)
        othernode.neighbors.append(self)

class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        self.graph[node] = node.neighbors
    def bfs(self, start):
        visited = []
        queue = []
        queue.append(start)
        visited.append(start)
        while queue:
            current = queue.pop(0)
            print(current.key, end = ' ')
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
    def dfs(self, start):
        visited = []
        stack = []
        stack.append(start)
        visited.append(start)
        while stack:
            current = stack.pop()
            print(current.key, end = ' ')
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.append(neighbor)
            

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")
node1.add_neighbor(node2)
node1.add_neighbor(node3)
node2.add_neighbor(node4)
node2.add_neighbor(node5)
node3.add_neighbor(node6)
node3.add_neighbor(node7)
node5.add_neighbor(node8)
node6.add_neighbor(node8)
graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
graph.add_node(node5)
graph.add_node(node6)
graph.add_node(node7)
graph.add_node(node8)
graph.bfs(node1)
print()
graph.dfs(node1)
'''