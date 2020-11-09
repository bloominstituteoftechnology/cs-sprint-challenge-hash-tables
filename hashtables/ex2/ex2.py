#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


dictionary = {}


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination

    start = dictionary['NONE']
    end = dictionary[start]
    for i in range(length):
        route.append(start)
        start = end
        end = dictionary[start]
    return route
