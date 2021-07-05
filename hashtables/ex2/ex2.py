#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dic = {}
    for ticket in tickets:
        dic[ticket.source] = ticket.destination
    
    route = []
    next_ = dic["NONE"]
    route.append(next_)
    while next_ != "NONE":
       next_ = dic[next_]
       route.append(next_)

    return route
