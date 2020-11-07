#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create hashtable
    hashtable = {}
    # create list to hold the route
    route = [None]*(length-1)

    # go through the tickets and map source and destrination
    for t in tickets:
        # if source is note put it as the first element in array (as the first destination)
        if t.source == "NONE":
            route[0] = t.destination
        # otherwise add to hashtable
        else:
            hashtable.update({t.source: t.destination})

    # go through the length and check if current key is the next key's value and append it
    for i in range(1, length-1):
        route[i] = hashtable[route[i-1]]

    return route



tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]

print(reconstruct_trip(tickets, 10))
