graph = {
    '8': ['2', '5'],
    '2': ['10', '6'],
    '5': ['9', '12'],
    '10': ['3'],
    '6': [],
    '9': [],
    '12': [],
    '3': []
}

print(graph)
vis = []
que = []

def bs(vis, graph, node):
  vis.append(node)
  que.append(node)

  while que:
    m = que.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in vis:
        vis.append(neighbour)
        que.append(neighbour)

print("Following is the Breadth-First Search")
bs(vis, graph, '2')


