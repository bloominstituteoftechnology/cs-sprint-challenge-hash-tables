#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Understand:
    tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
Your function should output an array of strings with the entire route of
your trip. For the above example, it should look like this:
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

    PLAN:
    Create a dict with source as key and destination as Values
    Starting point is Key will be None, then find its value. 
    This value will be the next key. 
    Return all the destination.
    """
    
    route = [None] * length
    ht = {}

    for ticket in tickets:
        ht[ticket.source] = ticket.destination #Step 1 in plan

    next_dest = ht["NONE"] # at start source is None

    for i in range(0,length):
        route[i] = next_dest # add the city to route list
        next_dest = ht[next_dest] # move onto pair where this is the source city, and append its dest

    return route
