#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = []
    
    hashtable = {}

    for t in tickets:
        hashtable[t.source] = t.destination

    route.append(hashtable['NONE'])

    for i in range(length - 1):
        if route[i] in hashtable:
            route.append(hashtable[route[i]])

    return route
