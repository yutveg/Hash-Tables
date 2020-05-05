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
        # create a node with our desired key and value
        new_entry = HashTableEntry(key, value)

        # create index to insert node
        index = self.hash_index(key)

        # if index is empty add node directly on index
        if self.storage[index] is None:
            print("hit none if")
            self.size += 1
            self.storage[index] = new_entry

        # if index is taken iterate through node-chain until we hit either None or an existing entry with same key to update
        else:
            cur_node = self.storage[index]
            while cur_node:
                
                # hit existing key entry
                if cur_node.key == new_entry.key:
                    print(f"{cur_node.key} changing value from {cur_node.value} to {new_entry.value}")
                    cur_node.value = new_entry.value
                    break
                # else, found empty spot
                if cur_node.next is None:
                    cur_node.next = new_entry

                cur_node = cur_node.next

        

        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.size == 0:
            return

        index = self.hash_index(key)

        if self.storage[index] is None:
            print("Key not found.")
            return
        # if we find key as first index, set current slot to reference next node aka None
        elif self.storage[index].key == key:
            if self.storage[index].next is None:
                self.size -= 1
            self.storage[index] = self.storage[index].next
            return
        # if slot taken and not our key, iterate through
        elif self.storage[index].key != key:
            # if only one node and not our key, key does not exist in chain
            if self.storage[index].next is None:
                print("Key not found.")
                return
            # iterate through chain
            prev_node = None
            cur_node = self.storage[index]
            while cur_node:
                # if we find key
                if cur_node.key == key:
                    # set previous node next to equal next node (possibly None)
                    # set current node to equal next node (possibly None) so it loses reference
                    prev_node.next = cur_node.next
                    self.storage[index] = cur_node.next
                    return

                prev_node = cur_node
                cur_node = cur_node.next
            print("Key not found.")
            return
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if self.size == 0:
            return None

        index = self.hash_index(key)

        if self.storage[index] is None:
            return None

        elif self.storage[index].key != key:
            cur_node = self.storage[index]
            while cur_node:
                if cur_node.key == key:
                    print(f"get key: {key} and value: {cur_node.value}")
                    return cur_node.value
                cur_node = cur_node.next
            # no key = return None
            return None
        # if we found key, return value
        else:
            print(f"get key: {key} and value: {self.storage[index].value}")
            return self.storage[index].value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        list_to_merge = [None] * self.capacity
        self.storage = self.storage + list_to_merge 
        self.capacity = self.capacity * 2
        for index in range(self.capacity):
            item = self.storage[index]
            if item != None:
                # we have hit a node
                cur_node = self.storage[index]
                while cur_node:
                    self.delete(self.storage[index])
                    self.put(cur_node.key, cur_node.value)
                    cur_node = cur_node.next
                
        
        


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
