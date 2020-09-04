#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # set up dict
    my_dict = {}
    # setting up list (route)
    route = [None] * length

    # go through all tickets
    for ticket in tickets:
        # set dict source
        my_dict[ticket.source] = ticket.destination
    # reset my dict
    next = my_dict["NONE"]

    for r in range(0, length):  # iterate through range
        # set route dict
        route[r] = next
        # set the next destination to dict
        next = my_dict[next]

    return route
