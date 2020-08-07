#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # routes looked up
    cache = {}
    # array with starting locations
    route = []
    for tick in tickets:
        cache[tick.source] = tick.destination
    # start key
    next = cache["NONE"]

    while next != "NONE":
        route.append(next)
        next = cache[next]
    route.append('NONE')
    return route


# Write a function `reconstruct_trip` to reconstruct your trip from your
# mass of flight tickets. Each ticket is represented as a class with the
# following form:

# ```


# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination


# ```
# Your function should output an array of strings with the entire route of
# your trip. For the above example, it should look like this:

# ```
# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
# ```

# Your solution should run in linear time. You can assume that your
# function will always be handed a valid ticket chain as input.
