#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #creating a dict
    store = {}
    #creating a list the len of the length
    route = [None] * length
    #iterating over the tickets
    for ticket in tickets:
        #setting the source in store to the destination
        store[ticket.source] = ticket.destination
    #resetting the destination
    destination = store['NONE']
    #iterating over the length
    for flight in range(length):
        #setting the route flight to the destination
        route[flight] = destination
        #setting the destination to the store
        destination = store[destination]


    return route
