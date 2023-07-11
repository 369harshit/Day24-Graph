INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = []
    for row in graph:
        dist.append(row[:])
      

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
graph = [
    [0, 2, INF, INF],
    [1, 0, 3, INF],
    [INF, INF, 0, INF],
    [3, 5, 4, 0]
]

distances = floyd_warshall(graph)
for row in distances:
    print(row)
