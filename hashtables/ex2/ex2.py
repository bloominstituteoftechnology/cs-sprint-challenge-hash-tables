#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [''] * length
    route_hash = {}

    for tix in tickets:
        if tix.source == "NONE":
            route[0] = tix.destination

        elif tix.destination == "NONE":
            route[length - 1] = tix.destination

        route_hash[tix.source] = tix.destination

    for i in range(len(route)):
        # print(route)
        if i == 0 or i == len(route) - 1:
          pass 
        else:
            route[i] = route_hash[route[i - 1]]

    print(route)
    return route
