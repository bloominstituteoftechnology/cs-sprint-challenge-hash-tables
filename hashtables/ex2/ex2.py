#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination


def reconstruct_trip(tickets, length):
    dict = {}
    route = []

    for ticket in tickets:
        # set the dictionary up with the origin as the key and destination as the value
        dict[ticket.origin] = ticket.destination
    # we know our first ticket has an origin of "NONE" so lets set our pointer
    pointer = dict["NONE"]
    # length is the number of tickets
    # repeat this loop until all tickets have been arranged
    while len(route) < length:
        # append the pointer to the array
        route.append(pointer)
        # change the pointer to the value of the destination - not the origin
        pointer = dict[pointer]

    return route
