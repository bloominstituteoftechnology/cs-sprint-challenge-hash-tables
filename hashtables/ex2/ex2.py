#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG"),
]


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = dict()

    for t in tickets:
        table[t.source] = t.destination

    route = []
    start = table["NONE"]
    route.append(start)

    while len(route) < length:
        for key in table:
            if key == route[-1]:
                route.append(table[key])

    return route


print(reconstruct_trip(tickets, 10))
