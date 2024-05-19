class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        
        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root
        while temp:
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:                            
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while queue:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return results
    
    def DFS_preorder(self):
        results = []
        
        def traverse(cur_node):
            results.append(cur_node.value)
            if cur_node.left:
                traverse(cur_node.left)
            if cur_node.right:
                traverse(cur_node.right)
        
        traverse(self.root)
        
        return results
    
    def DFS_postorder(self):
        results = []
        
        def traverse(cur_node):
            if cur_node.left:
                traverse(cur_node.left)
            if cur_node.right:
                traverse(cur_node.right)
                
            results.append()
        
        traverse(self.root)
        
        return results
    
    def DFS_inorder(self):
        results = []
        
        def traverse(cur_node):
            if cur_node.left:
                traverse(cur_node.left)
            results.append()
            if cur_node.right:
                traverse(cur_node.right)
        
        traverse(self.root)
        
        return results
        
        
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value, my_tree.root.left.value, my_tree.root.right.value)

#print(my_tree.BFS())
print(my_tree.DFS_preorder())