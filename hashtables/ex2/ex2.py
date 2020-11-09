#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # all tickets
    cache = {}
    # add all tickets to cache
    for t in tickets:
        cache[t.source] = t.destination
    # list that returns destination
    itinerary = []
    # which stop we're currently on
    current = 'NONE'
    for i in range(length):
        # append the value to the trip list
        itinerary.append(cache[current])
        # set a new current
        current = cache[current]
    return itinerary
