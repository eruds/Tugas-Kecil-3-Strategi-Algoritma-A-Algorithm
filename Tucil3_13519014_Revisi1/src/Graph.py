# Untuk visualisasi
import networkx as nx
import matplotlib.pyplot as plt

# Local
from Node import Node
from PriorityQueue import PriorityQueue

# Directed Graph 
class Graph :
    def __init__(self) : 
        # Node Coordinates 
        self.__nodes = {}

        # Untuk kebutuhan visualisasi dengan networkx dan matplotlib
        self.visual = []

        # Edges Weight/Priority  
        self.__adjacencyList = {}
    
    # Getter
    def getNodes(self) : 
        return self.__nodes;
    
    def getAdjacencyList(self) :
        return self.__adjacencyList;

    # Menampilkan semua node
    def printNodes(self) : 
        print("[ ", end="")
        for node in self.nodes : 
            print(node, end=" ")
        print(" ]")

    # Menambahkan simpul baru
    def addNode(self, nodeTitle, x, y) :
        newNode = Node(nodeTitle, x, y)
        self.__nodes[nodeTitle] = (newNode)
        self.__adjacencyList[newNode.title] = {}

    # Menambahkan sisi baru
    def addEdge(self, nodeStart, nodeEnd, weight) : 
        # Error Handling 
        if(type(nodeStart) != str or type(nodeEnd) != str ) : 
            raise Exception("Node argument must be a string")
        if(type(weight) != int) :
            if(weight != float('inf')) : 
                raise Exception("Weight argument must be an integer or infinity")
        self.__adjacencyList[nodeStart][nodeEnd] = weight

        if (weight != float('inf') and weight > -1):
            temp = [nodeStart, nodeEnd]
            self.visual.append(temp)

    # Mendapatkan jarak Eucledean
    def getEuclideanDistance(self, x1, x2, y1, y2) : 
        return ((x1 - x2)**2 + (y1 - y2)**2)**(0.5) 

    # Heuristik
    def getHeuristic(self, nodeStart, nodeEnd) :
        if(type(nodeStart) != Node or  type(nodeEnd) != Node) : 
            raise Exception("Argument must be an instance of Node Object")
        return self.getEuclideanDistance(nodeStart.x, nodeEnd.x, nodeStart.y, nodeEnd.y);

    # Mencari Shortest Path antara dua node. Tipe balikan berupa map berisi data path dan distance
    # Antara nodeStart dan nodeEnd
    def shortestPath(self, nodeStart, nodeEnd) : 
        if(type(nodeStart) != str or type(nodeEnd) != str) : 
            raise Exception("Shortest path node argument must be a string")
        # Shortest Path Using A* Algorithm 
        nodeSet = PriorityQueue()
        distances = {}
        previous = {} 
        visited = []
        # Initial State 
        nodeSet.enqueue(nodeStart, 0)
        previous[nodeStart] = None
        # Filling distances with inf 
        for node in self.__nodes : 
            if(node != nodeStart) : 
                distances[node] = float('inf') 
            else : 
                distances[nodeStart] = 0
        while not nodeSet.empty():
            currentNode = nodeSet.dequeue().item;
            if(currentNode == nodeEnd) : 
                path = []
                # distances = 0
                while(previous[currentNode] != None) : 
                    path.insert(0,currentNode);
                    currentNode = previous[currentNode];
                path.insert(0, nodeStart)
                return { 'path' : path, 'distance' : distances[nodeEnd] }

            # Filtering nodes that have inf distance
            adjacencyList = dict(filter(lambda node: node[1] != float('inf'), self.__adjacencyList[currentNode].items()))
            for neighbor in adjacencyList :
                # Continue the for loop if the neighbor is already visited
                if(neighbor in visited) : 
                    continue 
                weight = self.__adjacencyList[currentNode][neighbor] 
                if(weight == float('inf')) :
                    continue 
                candidateDistance = distances[currentNode] + int(weight)
                if(candidateDistance < distances[neighbor]) : 
                    # Adding neighbor to the previous map and distances map
                    previous[neighbor] = currentNode 
                    distances[neighbor] = candidateDistance

                    # Calculating the heuristic value between the starting node and the current neighbor.
                    nodeStartInput = self.__nodes[nodeStart]
                    neighborInput = self.__nodes[neighbor]
                    priority = distances[neighbor] + self.getHeuristic(nodeStartInput, neighborInput)
                    
                    # Add the current neighbor to the queue.
                    if not nodeSet.exists(neighbor) :  
                        nodeSet.enqueue(neighbor, priority)
            visited.append(currentNode)

    # Membuat graf dari file
    # This function only works with specific structure that is specified in the sample.txt file
    def setGraphFromFile(self, filename) : 
        # Read the file 
        f = open(filename, "r", encoding="utf-8")
        arr = f.readlines()
        temp = []
        for i in arr : 
            temp.append(i.rstrip())
        arr = temp
        nodeCount = int(arr[0])
        nodes = arr[1:nodeCount+1]
        adjacencyList = arr[nodeCount+1:]
        # Filling the self.__nodes attribute
        for node in nodes : 
            nodeAttributes = node.split();
            title = nodeAttributes[0]
            x = int(nodeAttributes[1])
            y = int(nodeAttributes[2])
            self.addNode(title, x, y);
        # Filling the self.__adjacencyList attribute;
        for connection in adjacencyList : 
            connectionList = connection.split();
            nodeStart = connectionList[0]
            for i in range(len(connectionList[1:])) : 
                key = list(self.__nodes.keys())[i]
                nodeEnd = self.__nodes[key].title
                weight = int(connectionList[1:][i])
                if(weight == -1) : 
                    weight = float('inf')
                self.addEdge(nodeStart, nodeEnd, weight)

    # Visualisasi dengan networkx dan matplotlib
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
