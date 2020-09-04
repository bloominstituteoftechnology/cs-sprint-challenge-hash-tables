#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Highlights from README:

    source (string) - starting airport
    destination (string) - destination airport

    pseudocode example:

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

    target output:
    an array of strings with the entire route of your trip
    for example above:

    ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

    """
    # Your code here

    cache = {}
    route = [None] * length
    for t in tickets:
        cache[t.source] = t.destination

    flightplan = cache['NONE']

    for flight in range(length):
        route[flight] = flightplan
        flightplan = cache[flightplan]

    return route
