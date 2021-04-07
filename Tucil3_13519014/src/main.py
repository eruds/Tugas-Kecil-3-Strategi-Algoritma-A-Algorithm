import random

# Local Import 
from Node import Node
from Graph import Graph

# Dengan mengasumsikan tiap case diberi nama Test1.txt, Test2.txt, dst 
# Automatic test yang akan menjalankan seluruh test case sekaligus dengan node awal dan akhir random.
def runTestCases(numOfCases) : 
    for i in range(numOfCases) : 
        filename = f"Test{i+1}.txt"
        graph = Graph()
        graph.setGraphFromFile("../test/" + filename)
        nodes = list(graph.getNodes().keys())
        length = len(nodes)
        n = random.randint(0,length-1)
        start = nodes[n]
        n = random.randint(0,length-1)
        end = nodes[n]
        result = graph.shortestPath(start, end)
        print(f"Test case number {i+1}")
        print(f"Selected nodes are : {start} and {end}")
        print("Path : " + str(result['path']))
        print("Distance : ", result['distance'])
        print()

def main() : 
    # Menjalankan seluruh test cases 
    numOfCases = 6
    runTestCases(numOfCases);

    # # Apabila ingin menjalankan test case satu per satu, uncomment bagian bawah dan comment runTestCases(numofCases)
    # # Tinggal memasukkan nama file beserta ekstensinya, Contoh: "Test1.txt"
    # filename = input("Masukkan nama file: \n")
    # graph = Graph()
    # graph.setGraphFromFile("../test/" + filename)

    # # Pastikan nama simpul sesuai dengan pada file input
    # start = input("Masukkan simpul asal: \n")
    # end = input("Masukkan simpul tujuan: \n")
    # result = graph.shortestPath(start, end)
    # print("Path : " + str(result['path']))
    # print("Distance : ", result['distance'])
    # print()
    

main()