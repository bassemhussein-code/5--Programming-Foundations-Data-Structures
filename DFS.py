class Graph():

    def __init__(self, edges, N):
        self.adjlist = [[]for _ in range(N)]

        for (src, dest) in edges:

            self.adjlist[src].append(dest)


def DFS(graph, v, visited):

    visited[v] = True

    for u in graph.adjlist[v]:
        if not visited[u]:
            DFS(graph, u, visited)


def check(graph, N):

    for i in range(N):

        visited = [False]*N

        DFS(graph, i, visited)

        for b in visited:
            if not b:
                return False

    return True


edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]


N = 5


'''construct the graph '''


#  construct the graph

graph = Graph(edges, N)


if check(graph, N):

    print('this is strongly connected graph')

else:

    print('this is not strongly connected graph')
