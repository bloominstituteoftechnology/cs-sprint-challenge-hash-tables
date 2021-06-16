#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    # route variable is an array with none value, which is then multiplied by len of list
    route = [None] * length
    # loop through the tickets
    for ticket in tickets:
        # We'll use this to get our destinations into our list
        # This is setting the source in cache to the destination
        cache[ticket.source] = ticket.destination
    next = cache["NONE"]
    # loop through the length of the list
    for current in range(0, length):
        # Grab the current index in route
        route[current] = next
        # Assign it our next variable
        next = cache[next]
    # The list is completed with correct routes so we can return it
    return route
