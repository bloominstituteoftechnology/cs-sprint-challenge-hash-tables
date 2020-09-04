#  Hint:  You may not need all of these.  Remove the unused functions.


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    route_dict = {}

    route = []

    for ticket in tickets:

        route_dict[ticket.source] = ticket.destination

    idx = 0
    curr_dest = "NONE"

    while idx < length:

        curr_dest = route_dict.get(curr_dest)
        route.append(curr_dest)
        idx += 1

    print(route)
    return route


# reconstruct_trip(tickets, 3)
