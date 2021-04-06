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
        start = input("Masukkan simpul asal: \n")
        end = input("Masukkan simpul tujuan: \n")
        path = graph.shortestPath(start, end)
        print(path)

def main() : 
    # Tinggal memasukkan nama file beserta ekstensinya, Contoh: "Test1.txt"
    filename = input("Masukkan nama file: \n")
    graph = Graph()
    graph.setGraphFromFile("../test/" + filename)

    # Pastikan nama simpul sesuai dengan pada file input
    start = input("Masukkan simpul asal: \n")
    end = input("Masukkan simpul tujuan: \n")
    path = graph.shortestPath(start, end)
    print(path)

main()