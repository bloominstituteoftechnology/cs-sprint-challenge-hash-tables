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
    cache = {}
    route = []

    # loop though the tickets and set cache from source to destination
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # cache needs to equal some to go thorough while loop
    destination = cache["NONE"]
    while destination != "NONE":
        #append the destion to the route and set that to the cache now
        route.append(destination)
        destination = cache[destination]
    # have to add NONE to the list
    route.append("NONE")
    return route
