#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    dict = {}
    for item in tickets:
        dict[item.source] = item.destination
    route = []

    next = dict["NONE"]
    route.append(next)

    for i in range(0, length):
        next = dict[next]
        print(next)
        route.append(next)
        if next == "NONE":
            break

    return route

