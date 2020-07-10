#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class HashTable:
    def __init__(self, capacity):
        self.size = capacity
        self.storage = [None] * capacity


def hash(x, max):
   x = ((x >> 16) ^ x) * 0x45d9f3b
   x = ((x >> 16) ^ x) * 0x45d9f3b
   x = ((x >> 16) ^ x)

   return x % max


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
    # tickets == HashTable
    # length ==
    # should return an array of strings with the entire route
    new_hash_table = HashTable(length)
    route = [None] * (length * 1)

    # traverse the tickets list and add each ticket
    for item in tickets:
        add(new_hash_table, item.source, item.destination)
    
    current_ticket = get(new_hash_table, "NONE")

    for i in range(0, length - 1):
        route[i] = current_ticket
        current_ticket = get(new_hash_table, current_ticket)

    return route
