class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        # add node to end
        if self.length > 0:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return_node = self.head
            self.head = None
            self.tail = None
        else:
            return_node = self.tail
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp

        self.length -= 1
        return return_node
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return_node = self.head
            self.head = None
            self.tail = None
        else:
            return_node = self.head
            self.head = return_node.next

        self.length -= 1
        return return_node
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif index >= 0 and index < self.length:
            temp = self.get(index-1)
            if temp:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                self.length += 1
                return True
        return False

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index > 0 and index < self.length - 1:
            temp = self.get(index-1)
            if temp:
                removing_node = temp.next
                temp.next = removing_node.next
                removing_node.next = None
                self.length -= 1
                return removing_node
        return None
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
            
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



# code for testing
linked_list = LinkedList(4)
linked_list.print_list()

node = linked_list.pop()
print("Popped", node.value)
linked_list.print_list()

linked_list.append(3)
linked_list.append(2)
linked_list.print_list()

node = linked_list.pop()
print("Popped", node.value)
linked_list.print_list()
print("Tail pointer", linked_list.tail.next)

linked_list.prepend(1)
print("Prepending 1")
linked_list.print_list()

pop_first_node = linked_list.pop_first()
print("Popped first")
print(pop_first_node.value)
print("-----")
linked_list.print_list()

print("testing insert")
linked_list.insert(0, 123)
linked_list.insert(2, 124)
linked_list.insert(1, 52)
linked_list.print_list()

print("testing removing")
linked_list.remove(1)
linked_list.remove(3)
linked_list.print_list()

print("reversing")
linked_list.reverse()
linked_list.print_list()