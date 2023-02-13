from itertools import permutations
from sys import maxsize


def Tsp(graph, startnode) :
    nodes = []
    path = []
    leng = len(graph)

    for i in range(leng) :
        if i != startnode :
            nodes.append(i)

    max_leng = maxsize
    next_permutation = permutations(nodes)

    for permutation in next_permutation :
        path_mes = 0
        s = startnode
        for element in permutation :
            path_mes += graph[s][element]
            s = element

        path_mes += graph[s][startnode]

        if max_leng > path_mes :
            max_leng = path_mes
            path.append(permutation)

    return max_leng, path


graph = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]
startnode = 3
result = Tsp(graph, startnode)

print('Minimum cost : ', result[0])

for i in result[1] :
    print('path :', startnode, i, startnode)
