#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # Hash for (source, destination)
    locations = {}
    # Init route
    route = [None] * length

    # Init Locations
    for i in range(length):
        source = tickets[i].source
        destination = tickets[i].destination

        # check for head
        if source == "NONE":
            route[0] = destination

        locations[source] = destination

    # Reconstruction Loop
    for j in range(length):
        # While not none
        if route[j - 1] is not None:
            # Check that the index behind current position matches the source to destination
            route[j] = locations[route[j-1]]

    # Return a list of destinations in order
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
print(reconstruct_trip(tickets, len(tickets)))