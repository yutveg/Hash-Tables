class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        str_bytes = str(key).encode()
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        for byte_of_data in str_bytes:
            hash = hash * FNV_prime
            hash = hash ^ byte_of_data
        
        hash &= 0xffffffffffffffff
        return hash
            


    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.size == self.capacity:
            return
        index = self.hash_index(key)
        self.storage[index] = (key, value)
        self.size += 1

        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.size == 0:
            return
        index = self.hash_index(key)
        self.storage[index] = None
        self.size -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if self.size == 0:
            return None
        index = self.hash_index(key)
        return self.storage[index][1]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        list_to_merge = [None] * self.capacity
        self.storage = self.storage + list_to_merge 
        self.capacity = self.capacity * 2
        print(self.capacity)
        for index in range(self.capacity):
            item = self.storage[index]
            if item != None:
                print(item)
                # set the spot in storage to None
                self.storage[index] = None
                # rehash item and insert
                self.put(item[0], item[1])
        
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
