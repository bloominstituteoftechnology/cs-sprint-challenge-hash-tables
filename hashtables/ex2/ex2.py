class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = {}
    route = []

    for t in tickets:
        ht[t.source] = t.destination
    
    curr = ht["NONE"]
    while curr != "NONE":
        route.append(curr)
        curr = ht[curr]
    route.append("NONE") # append last "NONE" for tests

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

reconstruct_trip(tickets, len(tickets))