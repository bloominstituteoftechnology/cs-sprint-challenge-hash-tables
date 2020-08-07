#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):


    # Create a dict
    store = {}

    # Create a list the len of the length
    route = [None] * length

    # Iterate over list of tickets
    for ticket in tickets:
        #set the source in store to the destination
        store[ticket.source] = ticket.destination
    # reset the destination
    destination = store['NONE']
    # iterate over the length
    for flight in range(length):
        # set the route flight to destination
        route[flight] = destination
        # set the destination to the store
        destination = store[destination]

    return route
