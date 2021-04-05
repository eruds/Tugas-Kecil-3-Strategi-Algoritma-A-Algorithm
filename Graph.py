import copy 

from Node import Node

# Directed Graph 
class Graph :
    def __init__(self) : 
        self.__nodes = []
        self.__adjacencyList = {}
    def printNodes(self) : 
        print("[ ", end="")
        for node in self.nodes : 
            print(node.title, end=" ")
        print(" ]")
    def addNode(self, node, x, y) : 
        # Error Handling. 
        if(type(node) != str ) : 
            raise Exception("Argument must be a string")
        newNode = Node(node, x, y)
        self.__nodes.append(newNode)
        self.__adjacencyList[newNode.title] = []
    def addEdge(self, nodeStart, nodeEnd, weight) : 
        # Error Handling 
        if(type(nodeStart) != str or type(nodeEnd) != str ) : 
            raise Exception("Node argument must be a string")
        if(type(weight) != int) :
            if(weight != float('inf')) : 
                raise Exception("Weight argument must be an integer or infinity")
        self.__adjacencyList[nodeStart].append({'node' : nodeEnd, 'weight' : weight})
    def getEuclideanDistance(self, x1, x2, y1, y2) : 
        return ((x1 - x2 )**2 + (y1 - y2)**2)**0.5 
    def getHeuristic(self, nodeStart, nodeEnd) :
        if(type(nodeStart) != Node or  type(nodeEnd) != Node) : 
            raise Exception("Argument must be an instance of Node Object")
        return getEuclideanDistance(nodeStart.x, nodeEnd.x, nodeStart.y, nodeEnd.y);
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
        for node in nodes : 
            nodeAttributes = node.split();
            title = nodeAttributes[0]
            x = nodeAttributes[1]
            y = nodeAttributes[2]
            self.addNode(title, x, y);
        for connection in adjacencyList : 
            connectionList = connection.split();
            nodeStart = connectionList[0]
            for i in range(len(connectionList[1:])) : 
                nodeEnd = self.__nodes[i].title
                weight = int(connectionList[1:][i])
                if(weight == -1) : 
                    weight = float('inf')
                self.addEdge(nodeStart, nodeEnd, weight)
        print(self.__nodes)
        print(self.__adjacencyList);