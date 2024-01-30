class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue():
    def __init__(self, value):
        new_node = Node(value=value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1
    
    def dequeue(self):
        
        if self.length == 0:
            return None
        elif self.length == 1:
            return_val = self.first
            self.first = None
            self.last = None
        else:
            return_val = self.first
            self.first = self.first.next
            
        return_val.next = None    
        self.length -= 1
        return return_val
        
    def print_queue(self):
        temp = self.first
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
        
queue = Queue(4)
queue.print_queue()

queue.enqueue(2)
queue.print_queue()

dequeue_val = queue.dequeue()
print(dequeue_val.value)

queue.print_queue()