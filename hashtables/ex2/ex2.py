#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    my_dict = {}
    route = []

    # populating hash map
    for ticket in tickets:
        my_dict[ticket.source] = ticket.destination

    # Creating route
    for _ in range(length):
        if not route:
            route.append(my_dict['NONE'])
        else:
            route.append(my_dict[route[-1]])

    return route
