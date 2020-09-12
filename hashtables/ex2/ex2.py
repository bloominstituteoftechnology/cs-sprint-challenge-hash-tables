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

    # setting up list (route)
    route = [None] * length #len of length

    #going thru the ticket in all tickets
    for ticket in tickets: 
        # setting source in my dictionary 
        cache[ticket.source] = ticket.destination #to the destination
    next = cache["NONE"] #resetting my dictionary 

    for r in range(0, length): # iterating thru the range (over the length)
        # set route flight to dictionary
        route[r] = next 
        # set the next destination to the dictionary
        next = cache[next]

    return route
