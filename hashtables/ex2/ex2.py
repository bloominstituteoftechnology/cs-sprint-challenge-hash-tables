#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create a hashtable
    cache = {}
    
    # for each ticket
    # cache[source] = destination
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    
    # initialize empty route, first entry is our ticket with source NONE
    route = []
    route.append(cache["NONE"])

    # Iterate through tickets, checking in constant time against cache
    for ticket in tickets:

        # Our next source is the last lcoation in our route
        _next = route[-1]
        # Grab that source's destination
        route.append(cache[_next])
        # if final location is NONE, we are done
        if route[-1] == "NONE":
            return route
