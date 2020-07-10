#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
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
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return hash % max


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


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashtable = HashTable(length)
    route = [None] * length

    for i in tickets:
        add(hashtable, i.source, i.destination)

    # initialize key to NONE and iterate through tickets, updating new key as previous value

    key = "NONE"

    for i in range(length):
        current_ticket = get(hashtable, key)
        key = current_ticket
        route[i] = current_ticket

    # remove the final NONE
    route.pop()
    return route
