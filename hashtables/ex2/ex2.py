#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = [None] * length
    # start points
    s = {}
    for i in range(length):
        s[tickets[i].source] = tickets[i].destination
    route[0] = s["NONE"]
    for i in range(1, length):
        route[i] = s[route[i - 1]]
    return route
