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

    route = []
    mess_of_tickets = {}
    # for each list of tickets, 
    # iterate through the list 
    for ticket in tickets:

        # put each tuple into a key:value pair dictionary
        mess_of_tickets[ticket.source] = ticket.destination

    # starting with key of none
    location = mess_of_tickets['NONE']
    while location:  
        # add the key of each pair to a list  
        route.append(location)
        # find correspond none's value key:value pair
        location = mess_of_tickets[location]
        if location == 'NONE':
            route.append(location)
            break

    # return the list
    return route
