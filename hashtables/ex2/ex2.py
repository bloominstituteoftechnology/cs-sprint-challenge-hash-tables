#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route_dict = {}
    for each in tickets:
        route_dict[each.source] = each.destination
    
    route = []
    next_stop = route_dict['NONE']
    while next_stop != 'NONE':
        route.append(next_stop)
        next_stop = route_dict[next_stop]
    route.append(next_stop) # 'NONE' still needs to be added to the route
    return route