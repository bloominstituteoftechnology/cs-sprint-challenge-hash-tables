#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Create an empty dict
    cache = {}

    # We'll set the route variable to an array with a null value, multiplied by the length of the list
    route = [None] * length

    # We'll loop through our tickets
    for ticket in tickets:
        # We'll use this to get our destinations into our list
        cache[ticket.source] = ticket.destination
    next = cache["NONE"]

    # We'll loop through the length of the list
    for current in range(0, length):
        # Grab the current index in our route
        route[current] = next
        # Assign it our next variable
        next = cache[next]
    # After our list has been filled with the proper routes, we'll return it
    return route

'''
"None" - "PDX"
"PDX" - "DCA"
"DCA" - "NONE"
'''
