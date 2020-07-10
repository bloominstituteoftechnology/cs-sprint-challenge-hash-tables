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
    #iterate through list
    #assign key of souce  and value of destination
    #get key = "NONE" 
        ##PRINT source or destination???
    #continue until "NONE"
    hashedTickets = {}
    route = [None] * length
    for i in range(length):
        hashedTickets[tickets[i].source] = tickets[i].destination
    location = hashedTickets['NONE']
    for i in range(length):
        route[i] = location
        location = hashedTickets[location]

    print('ROUTE: ', route)
    return route
