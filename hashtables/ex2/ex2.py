#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# Create a cache
cache = {}


def reconstruct_trip(tickets, length):
    # Traverse the ticket list and load the cache
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    # Create a results arr, preload the destination with no source
    route = [cache["NONE"]]

    # Traverse the cache by key, swapping the current dest for the new source
    # appendending the airport identifiers until dest is None
    curr = route[0]

    while cache[curr] != "NONE":
        dest = cache[curr]
        route.append(dest)
        curr = cache[curr]

    route.append("NONE")
    return route
