#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # put all the tickets in a dictionary
    route = {}
    for ticket in range(length):
        # we want the source and then the destination
        route[tickets[ticket].source] = tickets[ticket].destination

    trip = []
    current_destination = "NONE"
    
    # go through the route putting it in order
    while len(route) > 0:
        new_destination = route[current_destination]
        trip.append(route[current_destination])
        del route[current_destination]
        current_destination = new_destination

    return trip

