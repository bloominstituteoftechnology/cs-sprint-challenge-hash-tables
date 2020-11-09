#ex2.py



#  Hint:  You may not need all of these. Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    ticket_dict = {} 
    flights = [] 

    for ticket in tickets: 
        ticket_dict[ticket.source] = ticket.destination

    destination = ticket_dict['NONE']

    while destination != 'NONE':
        flights.append(destination)
        destination = ticket_dict[destination]
    
    flights.append(destination)

    return flights
