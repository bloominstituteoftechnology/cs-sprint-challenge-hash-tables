#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_dict = {}
    
    for i in range(length):
        ticket_dict[tickets[i].source] = tickets[i].destination

    route = []
    curr = ticket_dict["NONE"]

    # first ticket destinations source = "NONE"
    # final flight destination source = "NONE"

    while curr != "NONE":
        route.append(curr)
        curr = ticket_dict[curr]
    route.append(curr)

    return route
