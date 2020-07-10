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
    flights = {}
    route = [None] * length  # set up our route list with enough slots
    for i in range(0, length):
        current = tickets[i]
        # the starting location is the key and the destination is the value
        flights[current.source] = current.destination
    # set first flight in arr to flight w/ source "NONE"
    route[0] = flights["NONE"]
    # print(route[0], 'departion')
    route[1] = flights[route[0]]  # found by following the i - 1 hint in read me
    # print(route[1], 'first layover')
    if length > 2:
        for i in range(2, length):
            # the `i`th location in the route can be found by checking the hash
            # table for the `i-1`th location
            route[i] = flights[route[i - 1]]

    return route
