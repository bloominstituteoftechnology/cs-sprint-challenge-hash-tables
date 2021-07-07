#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}

def reconstruct_trip(tickets, length):
    route = [None] * length
   
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    destination = cache["NONE"]

    for index in range(length):
        route[index] = destination
        destination = cache[destination]
    return route


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE","LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]

print(reconstruct_trip(tickets, len(tickets)))