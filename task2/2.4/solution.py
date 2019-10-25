"""solution"""

from collections import defaultdict

class Graph:
    """implementation of graph"""

    def __init__(self, edges):
        self.node = defaultdict(list)
        for edge in edges:
            self.node[edge[0]].append(edge[1])
            self.node[edge[1]].append(edge[0])

#self.node = {keys ~ nodes}
#self.node[node] = {values connected to this key ~ destinations}

    def bfs(self):
        """breadth-first search"""
        
       visited = ''
        for node in self.node:
            if str(node) not in visited:
                print(node)
                visited += str(node)
            for vertex in self.node[node]:
                if str(vertex) not in visited:
                    print(vertex)
                   visited += str(vertex)

    #def dfs(self, v):
        #troubles with implementation.

    def check(self):
        """prints the Graph"""

        print(self.node)

if __name__ == "__main__":
    INPUT_EDGES = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [1, 6], [6, 7], [6, 8]]
    GRAPH = Graph(INPUT_EDGES)
    GRAPH.bfs() # result : 0 3 1 2 4 6 5 7 8
    print('\n')
    #graph.dfs(0) # result :
