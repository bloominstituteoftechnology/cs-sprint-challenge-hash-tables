#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    table = {}
    for i in range(length):
        table[tickets[i].source] = tickets[i].destination
    start = "NONE"

    def next_trip(destination):
        next_flight = table.get(destination)
        route.append(next_flight)
        return next_flight

    nt = next_trip(start)
    while nt != "NONE":
        nt = next_trip(nt)

    return route

