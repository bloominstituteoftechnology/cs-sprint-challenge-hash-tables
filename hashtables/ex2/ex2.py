#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ## set cache
    cache = {}

    # set up the list of routes
    route = [None] * length 

    ## grab all tickets and cycle through them
    for ticket in tickets:
        ## set tickets into cache and setting destination
        cache[ticket.source] = ticket.destination
    next = cache["NONE"] 

    for r in range(0, length):
        route[r] = next
        next = cache[next]
        print(route)
    return route
