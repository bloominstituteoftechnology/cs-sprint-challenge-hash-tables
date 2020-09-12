#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    This is O(2n) (one to fill the table, one to look up the table) this rounds
    out to O(n), linear time.
    The space complexity is O(2n) as well, one for the table, one for the
    return list.
    """
    # Your code here
    # convert to a table
    table = {}
    for t in tickets:
        table[t.source] = t.destination


    route = [None] * length
    key = 'NONE'
    for i in range(length):
        val = table[key]
        route[i] = val
        key = val

    return route
