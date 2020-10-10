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

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    destination = cache["NONE"]
    while destination != "NONE":
        route.append(destination)
        destination = cache[destination]

    route.append("NONE")
    return route
