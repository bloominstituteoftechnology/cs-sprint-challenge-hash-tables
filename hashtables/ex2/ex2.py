#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # we can store all the tickets in a cache. The Key being the source, and the value being the ticket.
    # Doing this way allows us to call the destination as we loop thru and continually update the current destination
    
    route = []
    cache = {t.source: t for t in tickets}

    # our first flight will always have a source of NONE so we want our destination to be NONE since the Source is key,
    # but we want to know what the first destination is.  
    destination = 'NONE'

    for i in range(length):
        # because we saved the ticket object as the value in our cache. we can call the attribute destination to update 
        # our next source as current destination
        destination = cache[destination].destination

        # append the destination to our route list and reloop
        route.append(destination)
        

    return route
