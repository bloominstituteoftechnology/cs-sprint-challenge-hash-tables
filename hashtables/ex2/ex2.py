from hashtable import (HashTable)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        HashTable.ht_put(ht, ticket.source, ticket.destination)
    for i in range(len(route)):
        route[0] = HashTable.ht_find(ht, "NONE")
        if i+1 >= len(route):
            return route
        else:
            
            route[i+1] = HashTable.ht_find(ht, route[i])

    return route
