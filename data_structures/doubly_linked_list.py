class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLinkedList():
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1
        return True
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
double_linked_list = DoublyLinkedList(7)
double_linked_list.append(5)
double_linked_list.print_list()