# Kelas isi/item priority queue
class PriorityQueueItem : 
    def __init__(self, item, priority) : 
        if(type(priority) != str and type(priority) != int and type(priority) != float) : 
            raise Exception("QueueItem priority must be a string or int or float") 
        self.item = item
        self.priority = priority
    def __str__(self) : 
        return "(" + str(self.item) + "," + str(self.priority) + ")"

# Kelas priority queue
class PriorityQueue : 
    def __init__(self) : 
        self.__values = []
        self.length = 0
    def __str__(self) : 
        text = "["
        for i in range(self.length):
            item = self.__values[i]
            text += str(item)
            if(i != self.length-1) : 
                text += ","
        text += "]"
        return text 

    # Menambahkan item baru ke dalam priority queue
    def enqueue(self, item, priority) : 
        newItem = PriorityQueueItem(item, priority)
        self.__values.append(newItem)
        self.length += 1
        self.sort()

    # Menghapus data dari priority queue
    def dequeue(self) : 
        item = self.__values.pop(0)
        self.length -= 1
        return item

    # Sort berdasarkan priority
    def sort(self) : 
        for i in range(self.length):
            for j in range(self.length):
                item1 = self.__values[i]
                item2 = self.__values[j]
                if(item1.priority < item2.priority) : 
                    temp = item1 
                    self.__values[i] = item2 
                    self.__values[j] = temp

    # Cek apakah ada item
    def exists(self, item) : 
        for val in self.__values : 
            if(val.item == item) : 
                return True
        return False 
    
    # Cek apakah kosong
    def empty(self) : 
        return self.length == 0