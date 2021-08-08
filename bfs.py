# BFS algorithm
# T(n) = O(|V|+|E|)

# same as dictionary just never raises KeyError
from collections import defaultdict

class Graph():

	# graph as an adjacenty list
	def __init__(self):
		self.graph = defaultdict(list)

	# method to add edges to the graph, main graph constructor
	def addEdge(self, v, u):
		self.graph[v].append(u)

	# runs Breath First Search on the graph, starts with vertex s
	def BFS(self, s):

		# make an array of booleans to keep the record of viisited vertices
		visited = [False]*(max(self.graph)+1)

		# queue to store active vertices
		queue = []

		# append the active vertex
		queue.append(s)

		# mark it as visited
		visited[s] = True

		# loop until queue is not empty
		while(queue):

			# pop the front of the queue
			s = queue.pop(0)
			print(s, end=" ")

			# visit all the adjacent vertex of s
			for i in self.graph[s] :
				if visited[i] == False :
					queue.append(i)
					visited[i] = True

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
g.BFS(2)