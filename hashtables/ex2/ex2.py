#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# create cache
cache = {}

def reconstruct_trip(tickets, length):
    """
    Reconstructs a trip given a list of tickets.
    Each tickect has a source and a destination.
    The ticket for the first flight has source=None.
    The ticket of the final flight has destination=None.

    Returns:
    -------
    An array of strings with the route of the trip
    """
    # create an empty list in which we will save the airports
    route = []

    # hash each ticket such that source is the key and destination is value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    
    # The first flight is the one that has source=None
    route.append(cache['NONE'])

    # add in route each flight
    for idx in range(length):
        # take the flight from cache
        if route[idx] in cache:
            # is it the first flight? If so, move on
            if cache[route[idx]] == route[0]:
                continue
            # add the next destination
            route.append(cache[route[idx]])
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

reconstruct_trip(tickets, 10)