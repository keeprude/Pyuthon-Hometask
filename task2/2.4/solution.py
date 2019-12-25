"""solution"""

from collections import deque

class Graph:
    """implementation of graph"""


    def __init__(self, edges):
        """РІ graph_list РЅР° i-РѕРј РјРµСЃС‚Рµ СЃС‚РѕРёС‚ РІРµСЂС€РёРЅР°(Р»РёСЃС‚) СЃ РїРѕРјРµС‚РєРѕР№ i, Р° РІ СЃР°РјРѕРј Р»РёСЃС‚Рµ 
        СѓРєР°Р·Р°РЅС‹ РїРѕРјРµС‚РєРё РІРµСЂС€РёРЅ, Рє РєРѕС‚РѕСЂС‹Рј РґР°РЅРЅР°СЏ РІРµСЂС€РёРЅР° РёРјРµРµС‚ РґРѕСЃС‚СѓРї."""


        self.graph_list = []
        for x in range (len(edges)):
            while len(self.graph_list) <= edges[x][0]:
                self.graph_list.append([])
            while len(self.graph_list) <= edges[x][1]:
                self.graph_list.append([])
            self.graph_list[edges[x][0]].append(edges[x][1])
            self.graph_list[edges[x][1]].append(edges[x][0])

    def help(self):
        """helpful lists for search"""

        
        self.visited = [False] * len(self.graph_list)
        self.depth = [-1] * len(self.graph_list)

    def dfs(self, current):
        """Depth-first search"""


        self.visited[current] = True
        print(current)
        for vertex in self.graph_list[current]:
            if not self.visited[vertex]:
                self.dfs(vertex)

    def bfs(self, current):
        """Breadth-first search"""


        self.depth[current] = 0
        q = deque()
        q.append(current)
        while q:
            current = q.popleft()
            print(current)
            for vertex in self.graph_list[current]:
                if self.depth[vertex] == -1:
                    q.append(vertex)
                    self.depth[vertex] = self.depth[current] + 1
        self.depth = [-1] * len(self.graph_list)


if __name__=="__main__":
    INPUT_EDGES = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [2, 6]]
    GRAPH = Graph(INPUT_EDGES)
    GRAPH.help()

    print("DFS:")
    GRAPH.dfs(0)
    print("\nBFS:") 
    GRAPH.bfs(0)
