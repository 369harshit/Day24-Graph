import heapq

def add_edge(graph, u, v, weight):
    if u in graph:
        graph[u].append((v, weight))
    else:
        graph[u] = [(v, weight)]
    if v in graph:
        graph[v].append((u, weight))
    else:
        graph[v] = [(u, weight)]

def prim(graph):
    start_vertex = 0

    mst = []  # Minimum Spanning Tree
    visited = set()
    heap = []

    visited.add(start_vertex)

    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(heap, (weight, start_vertex, neighbor))

    while heap:
        weight, u, v = heapq.heappop(heap)

        if v not in visited:
            mst.append((u, v, weight))
            visited.add(v)

            for neighbor, weight in graph[v]:
                heapq.heappush(heap, (weight, v, neighbor))

    return mst

def calculate_mst_weight(mst):
    total_weight = 0
    for u, v, weight in mst:
        total_weight += weight
    return total_weight

# Input
V = 5
edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]

graph = {}

for u, v, weight in edges:
    add_edge(graph, u, v, weight)

minimum_spanning_tree = prim(graph)
minimum_spanning_tree_weight = calculate_mst_weight(minimum_spanning_tree)

print("MST:", minimum_spanning_tree)
print("Total weight of MST:", minimum_spanning_tree_weight)
