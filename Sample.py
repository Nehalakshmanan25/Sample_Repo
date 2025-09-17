class Graph_matrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0] * vertices for _ in range (vertices)]
    
    def edge_undirected(self, v1, v2, weight):
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight
    def edge_directed(self, v1, v2, weight):
        self.adjMatrix[v1][v2] = weight

graph = Graph_matrix(4)
graph.edge_undirected(0, 1,10)
graph.edge_undirected(1, 2,20)
graph.edge_undirected(1, 3,30)
graph.edge_undirected(2, 3,40)  
print("UnDirected graph")
for i in graph.adjMatrix:
    print(i)
graph = Graph_matrix(4)
graph.edge_directed(0, 1, 10)   
graph.edge_directed(1, 2, 20)
graph.edge_directed(1, 3, 30)
graph.edge_directed(2, 3, 40)
print("Directed graph")
for i in graph.adjMatrix:
    print(i)