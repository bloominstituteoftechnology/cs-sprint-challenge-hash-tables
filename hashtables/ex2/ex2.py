# FINISHED BUT NOT OPTIMIZED############################################################################
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
    path = []
    for ticket in tickets:
        if ticket.source == 'NONE':
            path.append(ticket.destination)
    

    def findNext (cur):
        for ticket in tickets:
            
            if ticket.source == cur:
                path.append(ticket.destination)
                if ticket.destination == 'NONE':
                    return False
                else:
                    return True

    run = True
    while run == True:
        run = findNext(path[len(path)-1])
    return path

