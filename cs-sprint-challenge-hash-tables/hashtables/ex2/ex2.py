#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    
    route = [None] * length
    count = 0

    for i in range(length):
        if tickets[i].source == "NONE":
            route[count] = tickets[i].destination
    count += 1
    
    while route[length - 2] is None:
        for i in range(length):
            if tickets[i].source == route[count - 1]:
                route[count] = tickets[i].destination
                count += 1

    return route

