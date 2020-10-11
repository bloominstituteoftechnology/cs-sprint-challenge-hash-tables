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
    dict = {}
    route = []

    # insert routes in dictionary, assign NONE as first trip
    for i in tickets:
        dict[i.source] = i.destination
    ticket = dict["NONE"]
    # print(dict)

    while ticket != "NONE":  # loop until value is NONE which is the last route
        route.append(ticket)
        ticket = dict[ticket]
    route.append(ticket)

    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]
# print(reconstruct_trip(tickets, 3))
