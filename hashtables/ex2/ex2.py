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
    flight_path = {}
    route = [None] * length
    for ticket in tickets:
        if ticket.source == "NONE":
            route[0] = ticket.destination
        else:
            flight_path[ticket.source] = ticket.destination
    if length > 1:
        for i in range(1, length):
            route[i] = flight_path[route[i-1]]

    return route

"""
line 15: check for the start destination of our trip
line 16: add it to our `route` array as the first element
line 19: hash each ticket with the source as key and destination as value
line 20: if the tickets are greater than 1 then we need to check other wise we know our flight path
line 21: loop through our object, grabbing the source's associated destination and adding it to our route 
"""

