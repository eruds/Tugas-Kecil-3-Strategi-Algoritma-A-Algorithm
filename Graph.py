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
            raise Exception("Weight argument must be an integer")
        self.__adjacencyList[nodeStart].append({'node' : nodeEnd, 'weight' : weight})
    def getDistance(self, nodeStart, nodeEnd) : 
        return ((nodeStart.x - nodeEnd.x )**2 + (nodeStart.y - nodeEnd.y)**2)**0.5 
    def getDistanceMatrix(self) :
        distance = {}
        for node in self.adjacencyList : 
            distance = getDistance(node1, node2) 
    def setGraphFromFile(self, filename) : 
        # Read the file 
        f = open(filename, "r", encoding="utf-8")
        arr = f.readlines()
        temp = []
        for i in arr : 
            temp.append(i.rstrip())
        arr = temp
        print(arr)
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
                self.addEdge(nodeStart, nodeEnd, weight)
        print(self.__nodes)
        print(self.__adjacencyList);
            
    def writeGraphToFile(self, filename) : 
        # Open the file to write 
        f = open(filename, "w", encoding="utf-8")
        string = ""
        finishedFile = ""
        connections = self.connections

        # Iterate the graph 
        for key in connections : 
            string += "<" + key + ">"
            for node in connections[key] : 
                string += ",<" + node + ">"
            string += ".\n"
            finishedFile += string 
            string = ""
        
        # Write to the file 
        f.write(finishedFile)
        f.close()