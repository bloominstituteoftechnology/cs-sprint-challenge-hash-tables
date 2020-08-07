#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Params:
    -----
    tickets = list of jumbled Ticket classes (starting flight has source of "NONE" and 
    ending flight has destinatiton of "NONE")
    length = length of ticket lists

    Returns:
    -----
    list of organized flights

    """

    ticket_dict = dict()
    organized_flights = list()

    # iterate over all of the tickets and add to the dictionary
    # with the souce being the key and the destination being the value
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    # start with the value of the dict at source == NONE
    # for first flight
    destination = ticket_dict["NONE"]

    # go until destination equals NONE
    while destination != "NONE":
        # add the destination to the organized flights
        # then reassign destination to be the next value
        organized_flights.append(destination)
        destination = ticket_dict[destination]

    # tests require that NONE be added at the end
    organized_flights.append(destination)

    return organized_flights