from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src, dest):
        distances = [float('inf')] * self.V
        distances[src] = 0
        visited = set()
        predecessors = [-1] * self.V

        while len(visited) < self.V:
            min_distance = float('inf')
            min_vertex = -1
            for v in range(self.V):
                if v not in visited and distances[v] < min_distance:
                    min_distance = distances[v]
                    min_vertex = v

            if min_vertex == -1:
                break

            visited.add(min_vertex)

            if min_vertex == dest:
                break

            for neighbor, weight in self.graph[min_vertex]:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = min_vertex

        path = []
        curr_vertex = dest
        while curr_vertex != -1:
            path.append(curr_vertex)
            curr_vertex = predecessors[curr_vertex]
        path.reverse()

        return distances[dest], path

# Test the algorithm
g = Graph(6)
g.addEdge(1, 2, 2)
g.addEdge(2, 5, 5)
g.addEdge(2, 3, 4)
g.addEdge(1, 4, 1)
g.addEdge(4, 3, 3)
g.addEdge(3, 5, 1)

source = 1
destination = 5
shortest_distance, path = g.dijkstra(source, destination)

print("Shortest distance from vertex", source, "to vertex", destination, ":", shortest_distance)
print("Shortest path:", path)
