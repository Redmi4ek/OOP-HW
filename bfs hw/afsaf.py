from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

start_vertex = 'A'
start_vertex_2 ='B'
start_vertex_3 = 'C'
start_vertex_4 = 'D'
start_vertex_5 = 'E'

print(bfs(graph, start_vertex))
print(bfs(graph, start_vertex_2))
print(bfs(graph, start_vertex_3))
print(bfs(graph, start_vertex_4))
print(bfs(graph, start_vertex_5))