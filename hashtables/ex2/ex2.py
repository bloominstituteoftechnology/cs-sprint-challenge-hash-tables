#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Understand:
    To save time we have a test file lol

    Plan:
    create a dict with the source as the key and the destination as the values
    find the initial airport which would be the source be "NONE"
    """
    # Your code here
    dict_trip = {}
    route = []

    if len(tickets) == 0:
        print("No tickets, no route")
        return None

    for ticket in tickets:
        dict_trip[ticket.source] = ticket.destination

    airport = dict_trip["NONE"]

    i = 0
    while i < length:
        route.append(airport)
        i += 1
        airport = dict_trip[airport]

    return route
