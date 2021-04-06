import random 
import copy 

from Graph import Graph 

# Cek graf siklik/tidak
def checkAcyclic(node, graph, visited, origin) : 
    # Get the key 
    key = node if type(node) == str else node.title
    connection = graph.connections[key]

    # Add the current node to the visited node 
    visited.append(key)
    for node in connection : 
        if(node in visited) : 
            return False
        else :
            # If node has not been visited, check the node.
            return checkAcyclic(node, graph, visited, origin)

    # If all nodes has been visited return true 
    connection = graph.connections[origin.title]
    count = 0
    for node in connection : 
        if(node in visited) :
            count += 1 
    return count == len(connection)

# Buat graf asiklik
def generateAcyclicGraph(numberOfNodes, seed) : 
    graph = Graph()
    for i in range(numberOfNodes) :
        graph.addNode(f"C{i+1}")
    for i in range(seed) : 
        # Select a random node 
        number1 = random.randint(0, numberOfNodes-1)
        number2 = random.randint(0, numberOfNodes-1)
        while number1 == number2 : 
            number1 = random.randint(0, numberOfNodes-1)
            number2 = random.randint(0, numberOfNodes-1)
        
        # Create a temporary graph 
        tempGraph = copy.deepcopy(graph)
        node1 = tempGraph.nodes[number1]
        node2 = tempGraph.nodes[number2]
        connection = tempGraph.connections[node1.title]

        # Check if the current node has been connected before
        if(node2.title not in connection) : 
            tempGraph.addConnection(node1,node2)
            # Check if by adding the new connection, the graph has become cyclic 
            if(checkAcyclic(node1, tempGraph, [], node1)) : 
                # Add the connection to the actual graph 
                graph.addConnection(node1,node2)
    return graph

def generateTestCases(numOfCases, nodes) : 
    j = 0
    for i in range(numOfCases) : 
        graph = generateAcyclicGraph(nodes, 1000)
        result = graph.topologicalSort()
        # Pembuatan test case terbatas hanya pada test case yang memiliki setidaknya depth=8 
        if(len(result) == 8) : 
            graph.writeGraphToFile(f"./testCase/{j+1}.txt")
            j+= 1

def resultToText(result, filename) : 
    f = open(filename, "w", encoding="utf-8")
    string = ""
    finishedFile = ""
    i = 0
    for key in result : 
        string += "Semester " + str(i+1) + " : {"
        for node in result[key] : 
            string += " " + node + " "
        string += "}\n"
        finishedFile += string
        string = ""
        i += 1
    f.write(finishedFile)
    f.close()    
