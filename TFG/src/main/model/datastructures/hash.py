# AUTHOR: Juan Manuel Rey Escobar


class Hash:
    """ Creates a hash table structure """
    def __init__(self, size):
        self.hash_table = [[] for _ in range(size)]
        
    """ Inserts a key-value pair in the hash table """
    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]
        
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
            
        if key_exists:
            bucket[i] = ((key, value))
            
        else:
            bucket.append((key, value))
            
    """ Searchs data from the hash table """
    def search(self, key):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
            
    """ Deletes a key-value pair from the hash table """   
    def delete(hash_table, key):
        hash_key = hash(key) % len(self.hash_table)    
        key_exists = False
        bucket = self.hash_table[hash_key]
        
        for i, kv in enumerate(bucket):
            k, v = kv 
            if key == k:
                key_exists = True 
                break
            
        if key_exists:
            del bucket[i]
            print ('Key {} deleted'.format(key))
            
        else:
            print ('Key {} not found'.format(key))  
            
        
            
            
            