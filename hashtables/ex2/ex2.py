#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


cache = {}

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # creating empty array
    array = []

    # for each ticket in the tickets array<,
    # add the ticket source as the key, and 
    # the ticket destination as the value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    array.append(cache['NONE'])

    for index in range(length):
        if array[index] in cache:
            if cache[array[index]] == array[0]:
                continue
            array.append(cache[array[index]])

    return array



    return route
