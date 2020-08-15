#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    trip_tics = {}
    for i in tickets:
        trip_tics[i.source] = i.destination
    route_list = []
    while len(route_list) < length:
        if len(route_list) == 0:
            x = trip_tics["NONE"]
            route_list.append(x)
        elif len(route_list) > 0:
            y = route_list[len(route_list)-1]
            z = trip_tics[y]
            route_list.append(z)
    return route_list
