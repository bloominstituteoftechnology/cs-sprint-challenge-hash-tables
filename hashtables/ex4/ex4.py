class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.size = capacity
        self.storage = [None] * capacity


def hash(string, max):
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)

   return x % max

def delete(hash_table, key):
    node = hash(key, len(hash_table.storage))

    current_node = hash_table.storage[node]
    last_node = None

    while current_node is not None and current_node.key != key:
        last_node = current_node
        current_node = last_node.next

    if current_node is None:
        print("ERROR: Unable to remove entry with key " + key)
    else:
        if last_node is None:  # Removing the first element in the LL
            hash_table.storage[node] = current_node.next
        else:
            last_node.next = current_node.next


def add(hash_table, key, value):
    node = hash(key, len(hash_table.storage))

    current_node = hash_table.storage[node]
    last_node = None

    while current_node is not None and current_node.key is not key:
        last_node = current_node
        current_node = last_node.next

    if current_node is not None:
        current_node.value = value
    else:
        new_node = LinkedList(key, value)
        new_node.next = hash_table.storage[node]
        hash_table.storage[node] = new_node


def get(hash_table, key):
    node = hash(key, len(hash_table.storage))

    current_node = hash_table.storage[node]

    while current_node is not None:
        if current_node.key == key:
            return current_node.value
        current_node = current_node.next

def resize(hash_table):
    new_hash_table = HashTable(2 * len(hash_table.storage))

    current_node = None

    for i in range(len(hash_table.storage)):
        current_node = hash_table.storage[i]
        while current_node is not None:
            add(new_hash_table, current_node.key, current_node.value)
            current_node = current_node.next

    return new_hash_table


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
