#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    for a in tickets:
        cache[a.source] = a.destination
    
    route = [cache['NONE']]
    
    index = 0
    current = route[index]
    while current != 'NONE':
        route.append(cache[route[index]])
        
        index += 1
        current = cache[route[index]]
    
    route.append(cache[route[index]])

    return route