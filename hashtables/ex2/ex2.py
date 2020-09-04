#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trip = {}
    trip_rev = {}
    start_point = ''
    for i in tickets:
        trip[i.source] = i.destination
        trip_rev[i.destination] = i.source
    i = 0

    origin = 'NONE'
    output_string = [trip['NONE']]
    i += 1
    while i != length:
        output_string.append(trip[output_string[-1]])
        i += 1


    return output_string
