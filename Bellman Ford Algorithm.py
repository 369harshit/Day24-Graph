class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, source):
        # Step 1: Initialize distances from source to all other vertices as infinity
        dist = [float('inf')] * self.V
        dist[source] = 0

        # Step 2: Relax all edges V-1 times
        for i in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]  # Graph contains negative-weight cycle

        return dist

# Example usage
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(1, 5, -3)
g.add_edge(2, 4, 3)
g.add_edge(3, 2, 6)
g.add_edge(5, 3, 1)
g.add_edge(1, 2, -2)
g.add_edge(3, 4, -2)

source_vertex = 0
distances = g.bellman_ford(source_vertex)
print("Shortest distances from source vertex", source_vertex)
print(distances)
