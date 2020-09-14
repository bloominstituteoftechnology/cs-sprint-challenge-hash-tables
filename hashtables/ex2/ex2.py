#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Create cache
    set up list to length
    for each ticket set starting location as key and destination as va;ue
    iterate over the length of the dictionary and set by the next destination.
    """
    cache = {} 
    route = [None] * length 

    for ticket in tickets: 
        cache[ticket.source] = ticket.destination
        
    next = cache["NONE"]

    for i in range(length):
        route[i] = next 
        next = cache[next]

    return route
