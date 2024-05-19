class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
        
    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
            
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is None:
            return None
        
        for item in self.data_map[index]:
            if item[0] == key:
                return item
        
        return None
    
    def keys(self):
        all_keys = []
        for item in self.data_map:
            if item is not None:
                for j in item:
                    all_keys.append(j[0])
        
        return all_keys
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
hash_table = HashTable()
hash_table.set_item('one', 1)
hash_table.set_item('two', 2)
hash_table.set_item('three', 3)

hash_table.print_table()

print(hash_table.get_item('three'))
print(hash_table.keys())