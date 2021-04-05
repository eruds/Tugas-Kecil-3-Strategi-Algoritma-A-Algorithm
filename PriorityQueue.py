class PriorityQueueItem : 
    def __init__(self, item, priority) : 
        if(type(priority) != str or type(priority) != int) : 
            raise Exception("QueueItem priority must be a string or int") 
        self.item = item
        self.priority = priority
    def __str__(self) : 
        return "(" + self.item + "," + self.priority + ")"

class PriorityQueue : 
    def __init__(self) : 
        self.values = []
    def enqueue(self, item, priority) : 
        print(item, priority) 