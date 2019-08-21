from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation

class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        self.userPath = []
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(id(path))
            self.userPath.append(path[:])
            #print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
                    # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        #self.path = []

        # Call the recursive helper function to print all paths
        #print("path_id",id(path))
        self.printAllPathsUtil(s, d, visited,[])

        return self.userPath


userFriendsMatrix = {0: [1, 2, 3], 2: [0, 1], 1: [3]}
graph = Graph(4)
for userId in userFriendsMatrix:
    userFriendsList = userFriendsMatrix[userId]
    for friend in userFriendsList:
        graph.addEdge(userId, friend)
print(graph)
s = 2
d = 3
userPath = graph.printAllPaths(s, d)
print(userPath)
# Graph.userPath
# print(Graph.userPath)
# print(graph.userPath)
# print(graph.graph)
# print(userPath)
