from Node import Node
from Graph import Graph
from utils import generateTestCases, resultToText

import os 
# Dengan mengasumsikan tiap case diberi nama Test1.txt, Test2.txt, dst 
def runTestCases(numOfCases) : 
    for i in range(numOfCases) : 
        filename = f"Test{i+1}.txt"
        graph = Graph()
        graph.setGraphFromFile("Test_Case/" + filename)
        graph.shortestPath('A', 'F')
def main() : 
    numOfCases = 2
    runTestCases(numOfCases)

main()