# Depth First Search
# T(n) = O(|V| + |E|), |V| = Number of vertices, |E| = Number of Edges

from collections import defaultdict

class Graph():

	# graph as an adjacency list
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, v, u):
		''' Adds edges in the graph '''
		self.graph[v].append(u)

	def DFSrecurse(self, visited, v):
		''' Explore the nodes in depth first manner, recursively '''

		# array to keep track of visited nodes
		visited.append(v)
		# print the visited node
		print(v, end=" ")

		# loop until all the unvisited neighbouring nodes of v is visited
		for i in self.graph[v]:
			if i not in visited :
				visited.append(i)
				self.DFSrecurse(visited,i)

	def DFS(self, v):
		''' starts DFS '''
		visited = []

		self.DFSrecurse(visited, v)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 2)
g.addEdge(4, 3)
g.addEdge(5, 3)
g.DFS(2)