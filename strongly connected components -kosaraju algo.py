from collections import defaultdict

# Graph class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # DFS function
    def DFS(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    # Transpose the graph
    def transposeGraph(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    # Kosaraju's algorithm
    def kosarajuAlgorithm(self):
        visited = [False] * self.V

        # First DFS to fill the stack
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.fillStack(i, visited, stack)

        # Transpose the graph
        gr = self.transposeGraph()

        # Mark all the vertices as not visited for the second DFS
        visited = [False] * self.V

        # Counter variable for SCCs
        count = 0

        # Perform DFS on the transposed graph in the order defined by the stack
        while stack:
            v = stack.pop()
            if visited[v] == False:
                gr.DFS(v, visited)
                count += 1

        return count

    # Fill vertices into the stack
    def fillStack(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.fillStack(i, visited, stack)

        stack.append(v)


# Test the algorithm
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Number of Strongly Connected Components:", g.kosarajuAlgorithm())
