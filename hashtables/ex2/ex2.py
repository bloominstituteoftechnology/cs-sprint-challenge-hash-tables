#  Hint:  You may not need all of these.  Remove the unused functions.


# in hash, starting location is the key and destination is value
# for ticket 1: {NONE: PDX}


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length
    # initialize array of route with the length of the route

    ht = {}
    # make a hash table to store the trip sources and destinations

    for t in tickets:
        # for every Ticket in tickets, set the key as the source and the destination as the value
        ht[t.source] = t.destination

    # what is the destination which has "NONE" as the key, meaning the starting ticket?
    next_destination = ht["NONE"]
    # so now the next_destination is the VALUE in the hash table in which the KEY is "NONE"... this is the start destination, which is the first one to add to the array

    # i is current ticket
    for i in range(0, length):
        # add value to array
        route[i] = next_destination

        next_destination = ht[next_destination]
        # the next destination is the VALUE in the hash table in which the KEY is the destination just added to the array, which will be the next leg of the trip... keep doing this until at the end of the length of tickets(trip)

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]

print(reconstruct_trip(tickets, 3))
