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
    route = [None] * length
    cache = {}
    for t in tickets: 
        cache[t.source] = t.destination
    dest = cache["None"]

    for flight in range(0, length): 
        route[flight] = dest
        dest = cache[dest]
    return route
