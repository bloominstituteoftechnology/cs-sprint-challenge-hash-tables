#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    create hashtable for origin key, destin value
    for key is none, push value to list
    for key as the previous value, push destin value
    for key as the previous valus, push the destin value...
    until you get the detine None 
    return the list
    """
    # Your code here
    hash_travel = {}
    route = []
    for ticket in tickets:
       hash_travel[ticket.source] = ticket.destination
    destin = hash_travel['NONE']

    while destin != 'NONE':
        route.append(destin)
        destin = hash_travel[destin]  # searching for destination with key destin

     

    return route

if __name__  == '__main__':
    tickets = [
        Ticket("PIT", "ORD"),
        Ticket( "XNA",  "CID" ),
        Ticket(  "SFO",  "BHM"),
        Ticket(  "FLG",  "XNA"),
        Ticket(  "NONE",  "LAX"),
        Ticket( "LAX",  "SFO"),
        Ticket( "CID",  "SLC"),
        Ticket( "ORD",  "NONE"),
        Ticket( "SLC",  "PIT"),
        Ticket( "BHM",  "FLG")
        
    ]
        
    print(reconstruct_trip(tickets, 10))