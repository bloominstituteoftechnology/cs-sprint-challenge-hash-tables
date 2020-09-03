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
    #set up dictionary
    my_dict = {} 

    # setting up list (route)
    route = [None] * length #len of length

    #going thru the ticket in all tickets
    for ticket in tickets: 
        # setting source in my dictionary 
        my_dict[ticket.source] = ticket.destination #to the destination
    next = my_dict["NONE"] #resetting my dictionary 

    for r in range(0, length): # iterating thru the range (over the length)
        # set route flight to dictionary
        route[r] = next 
        # set the next destination to the dictionary
        next = my_dict[next]
    return route
