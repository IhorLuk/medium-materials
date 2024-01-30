class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack():
    def __init__(self, value: int):
        new_node = Node(value=value)
        self.top = new_node
        self.height = 1
    
    def push(self, value: int) -> None:
        new_node = Node(value)
        
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node            
            
        self.height += 1
    
    def pop(self) -> Node:
        
        if self.height == 0:
            top_node = None
        else:
            top_node = self.top
            self.top = self.top.next
            top_node.next = None
        
        self.height -= 1
        return top_node
    
    def print_stack(self):
        temp = self.top
        for _ in range(self.height):
            print(temp.value)
            temp = temp.next
            
stack = Stack(2)
stack.push(3)
top_node = stack.pop()

stack.print_stack()
print("Pop: ", top_node.value)