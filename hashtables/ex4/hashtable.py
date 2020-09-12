class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.bucket = [None] * capacity

    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def ht_put(self, key, value):
        index = self.hash_index(key)
        current_pair = self.bucket[index]
        last_pair = None

        while current_pair is not None and current_pair.key != key:
            last_pair = current_pair
            current_pair = last_pair.next

        if current_pair is not None:
            current_pair.value = value
        else:
            new_pair = HashTableEntry(key, value)
            new_pair.next = self.bucket[index]
            self.bucket[index] = new_pair

    def ht_remove(self, key):
        index = self.hash_index(key)
        current_pair = self.bucket[index]
        last_pair = None

        while current_pair is not None and current_pair.key != key:
            last_pair = current_pair
            current_pair = last_pair.next

        if current_pair is None:
            return None
        else:
            if last_pair is None:
                self.bucket[index] = current_pair.next
            else:
                last_pair.next = current_pair.next

    def ht_find(self, key):
        index = self.hash_index(key)
        current_pair = self.bucket[index]

        while current_pair is not None:
            if(current_pair.key == key):
                return current_pair.value
            current_pair = current_pair.next

    def resize(self):
        new_hash_table = HashTable(2 * len(self.bucket))

        cur = None

        for i in range(len(self.bucket)):
            cur = self.bucket[i]
            while cur is not None:
                ht_put(new_hash_table,
                                cur.key,
                                cur.value)
                cur = cur.next

        return new_hash_table