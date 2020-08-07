class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        if type(capacity) is str:
            print('this needs to be an integer')

        self.capacity = capacity
        self.table = [None] * int(capacity)
        self.size = 0

    def get_num_slots(self):
        # Your code here
        return self.capacity

    def get_load_factor(self):
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5)+hash)+ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # Your code here
#Day 1:
        # key_hash = self.hash_index(key)
        # self.table[key_hash] = value
#Day 2:
        # after hashing, use that hash as the index
        index = self.hash_index(key)
        node = self.table[index]

        if node is None:
            self.table[index] = HashTableEntry(key, value)
            self.size += 1
        else: 
            while node:
                current = node

                # check if key already exists, if so, update with new value
                if current.key == key:
                    current.value = value
                    return value

                # if was not found and reached end, create new entry
                if current.next == None:
                    current.next = HashTableEntry(key, value)
                    # increase size by 1
                    self.size +=1
                    return current.next.value

                node = current.next

        if self.get_load_factor() > 0.7:
            # print(f'LOAD_FACTOR : {self.get_load_factor()}')
            self.resize(self.capacity * 2)
            

    def delete(self, key):
        # Your code here

        # key_hash = self.hash_index(key)
        # self.table[key_hash] = None

        # after hashing, use that hash as the index
        index = self.hash_index(key)
        node = self.table[index]

        if node == None:
            print(f'{key} does not exist in hash table')
            return None

        while node:
            current = node

            if current.key == key:
                self.table[index] = current.next
                self.size -= 1

            node = current.next


    def get(self, key):
        # Your code here

        # key_hash = self.hash_index(key)
        # return self.table[key_hash]

        # after hashing, use that hash as the index
        index = self.hash_index(key)
        node = self.table[index]

        # if index is empty, return none
        if node == None:
            return None
        
        while node:
            if node.key == key:
                return node.value
            node = node.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # for i in self.table:
        #     print(f'element: {i}')

        resized = HashTable(new_capacity)

        for index in self.table:
            if index:
                current = index
                while current:
                    # store its key/value into new hash table
                    resized.put(current.key, current.value)
                    # if so, change current to it
                    current = current.next
                    # if non next, move to next index
        
        self.capacity = new_capacity
        self.table = resized.table
                    
            

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def find(self, key):
#         current = self.head

#         if current is None:
#             return None

#         while current:
#             if current.key == key:
#                 return current
#             current = current.next

#         return current

#     def add_to_head(self, key, value):
#         current = self.head

#         #traverse list to see if key already exists
#         while current:
#             #if key is found, replace the current value with new value
#             if current.key == key:
#                 current.value == value
#                 return
#             current = current.next

#         # make new node if not in list (after traversing list)
#         new_node = HashTableEntry(key, value)
#         new_node.next = self.head
#         self.head = new_node

#     def add_to_tail(self, key, value):
#         current = self.head

#         while current:
#             #if key is found, replace the current value with new value
#             if current.key == key:
#                 current.value == value
#                 return

#             current = current.next

#             # make new node if not in list (after traversing list)
#             if current.next == None:
#                 new_node = HashTableEntry(key, value)
#                 current.next = new_node


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
