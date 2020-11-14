#  Hint:  You may not need all of these.  Remove the unused functions.
from collections import deque

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    dict = {}
    for ticket in tickets:
        t = {ticket.source:ticket.destination}
        dict.update(t)
        
    
    route = []
    firstdestination = dict.pop("NONE")
    route.append(firstdestination)
    curr = route[0]
    for ticket in dict:
        nextdestination = dict.get(curr)
        route.append(nextdestination)
        curr = route[route.index(curr)+1]
    # route.remove('NONE')
    

    return route

tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

print(reconstruct_trip(tickets,len(tickets)))