#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Input: List of tickest where each ticket is a dict with source airport and destination airport
    
    Output: ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
    """

    # initial cache/hash table
    cache = {}
    # loop through tickets
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    # final destination = NONE
    route = [cache["NONE"]]
    
    # get tickets in list of tickets to find next locations
    for ticket in tickets:
        
        next_destination = route[-1]
        
        # append next_destination from cache
        route.append(cache[next_destination])
    
        # when final route is None, append and return trip
        if route[-1] == "NONE":
            return route

