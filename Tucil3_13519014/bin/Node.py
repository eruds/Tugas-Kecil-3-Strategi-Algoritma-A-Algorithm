# Kelas simpul
class Node : 
    def __init__(self, title, x, y) : 
        if(type(title) != str ) : 
            raise Exception("Node title argument must be a string")
        if(type(x) != int or type(y) != int) : 
            raise Exception("X and Y argument must be an integer")
        self.title = title
        self.x = x
        self.y = y
    def __str__(self) : 
        return "(" + self.title + "," + str(self.x) + "," + str(self.y) + ")"

        