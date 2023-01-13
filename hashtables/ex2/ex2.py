#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    d = {}
    route = []
    
    for t in tickets:
        #mapping 
        if t.source not in d.keys():
            d[t.source] = t.destination
     #destination       
    route.append(d["NONE"])
    
    for i in range(1, length):
        route.append(d[route[i-1]])


    return route
