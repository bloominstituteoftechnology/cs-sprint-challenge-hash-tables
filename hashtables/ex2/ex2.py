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
    #set my hash table& define the route length
    hash_table = {}
    route = [None] * length
    
    for ticket in tickets:
        # push ticket info into hash table
        hash_table[ticket.source] = ticket.destination
    
    #turn hash table into lists of keys and values
    source = list(hash_table.keys())
    destination = list(hash_table.values())
    
    #set the route to start at none and set the 2nd position to 1st position
    route[0] = hash_table["NONE"]
    route[1] = hash_table[route[0]]
    
    #iterate over the route - find the ith location and subtract 1
    if length > 2:
        for i in range(2, length):
            route[i] = hash_table[route[i - 1]]

    return route
