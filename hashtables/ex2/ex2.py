#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    ticket = None
    for paper in tickets:
        hash_table_insert(hashtable, paper.source, paper)
        if paper.source == "NONE":
            ticket = paper

    counter = 0
    while ticket.destination != "NONE":
        route[counter] = ticket.destination
        counter += 1
        ticket = hash_table_retrieve(hashtable, ticket.destination)
    j = route
    j.append("NONE")
    # print(j)
    return route
