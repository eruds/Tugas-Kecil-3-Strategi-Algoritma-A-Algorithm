class PriorityQueueItem : 
    def __init__(self, item, priority) : 
        if(type(priority) != str and type(priority) != int and type(priority) != float) : 
            raise Exception("QueueItem priority must be a string or int or float") 
        self.item = item
        self.priority = priority
    def __str__(self) : 
        return "(" + str(self.item) + "," + str(self.priority) + ")"

class PriorityQueue : 
    def __init__(self) : 
        self.values = []
        self.length = 0
    def __str__(self) : 
        text = "["
        for i in range(self.length):
            item = self.values[i]
            text += str(item)
            if(i != self.length-1) : 
                text += ","
        text += "]"
        return text 
    def enqueue(self, item, priority) : 
        newItem = PriorityQueueItem(item, priority)
        self.values.append(newItem)
        self.length += 1
        self.sort()
    def dequeue(self) : 
        item = self.values.pop(0)
        self.length -= 1
        return item
    def sort(self) : 
        for i in range(self.length):
            for j in range(self.length):
                item1 = self.values[i]
                item2 = self.values[j]
                if(item1.priority < item2.priority) : 
                    temp = item1 
                    self.values[i] = item2 
                    self.values[j] = temp
    def exists(self, item) : 
        for val in self.values : 
            if(val.item == item) : 
                return True
        return False 
    def empty(self) : 
        return self.length == 0