class Node : 
    def __init__(self, title, x, y) : 
        self.title = title
        self.x = x
        self.y = y
    def __str__(self) : 
        return "(" + self.title + "," + self.x + "," + self.y + ")"

        