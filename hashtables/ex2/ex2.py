#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    store = {}
    route = []
    for each in tickets:
        source = each.source
        store[source] = each.destination

        board = wsr

        while board is not "NONE":
            route.append(board)
            board = store[board]
        route.append(board)
        return route
