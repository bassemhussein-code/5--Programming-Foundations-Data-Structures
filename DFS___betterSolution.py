class Graph():

    def __init__(self, edges, N):

        self.adjlist = [[]for _ in range(N)]

        for (src, dest) in edges:

            self.adjlist[src].append(dest)


def DEF(graph, v, visited):
    visited[v] = True

    for u in graph.adjlist[v]:

        if not visited[u]:

            DEF(graph, u, visited)


def check(graph, N):

    visited = [False]*N

    v = 0

    DEF(graph, v, visited)

    for b in visited:
        if not b:
            return False

    ''' reset the visited list '''

    visited = [False] * N

    edges = [(j, i)for i in range(N) for j in graph.adjlist[i]]

    '''reset the graph'''

    gr = Graph(edges, N)

    DEF(graph, v, visited)

    for b in visited:
        if not b:
            return False

    return True


edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]

N = 5


graph = Graph(edges, N)


if check(graph, N):
    print('this is a strongly connected graph')

else:
    print('this is not a strongly connected graph')
