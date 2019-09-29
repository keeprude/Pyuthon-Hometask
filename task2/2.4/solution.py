from collections import defaultdict

class Graph:
    def __init__(self, edges) :
        self.node = defaultdict(list)
        for edge in edges :
            self.node[edge[0]].append(edge[1])
            self.node[edge[1]].append(edge[0])

#self.node = {keys ~ nodes}
#self.node[node] = {values connected to this key ~ destinations}
    def bfs(self) :
        visited = ''
        for node in self.node :
            if not str(node) in visited :
                print(node)
                visited += str(node)
            for x in self.node[node] :
                if not str(x) in visited :
                    print(x)
                    visited += str(x)

    def dfs(self, v) :
        #troubles with implementation.

    def check(self) :
        print(self.node)

edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [1, 6], [6, 7], [6, 8]]
graph = Graph(edges)
graph.bfs() # result : 0 3 1 2 4 6 5 7 8
print('\n')
graph.dfs(0) # result : 

