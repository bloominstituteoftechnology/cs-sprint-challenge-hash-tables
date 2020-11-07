#  Hint:  You may not need all of these.  Remove the unused functions.

#don't know route
#each ticket is a class with source and destination value
#first flight source = None, final flight has a destination = None.

#output an array of strings with the entire route of your trip

'''

        ticket_1 = Ticket("PIT", "ORD")
        ticket_2 = Ticket("XNA", "SAP")
        ticket_3 = Ticket("SFO", "BHM")
        ticket_4 = Ticket("FLG", "XNA")
        ticket_5 = Ticket("NONE", "LAX")
        ticket_6 = Ticket("LAX", "SFO")
        ticket_7 = Ticket("SAP", "SLC")
        ticket_8 = Ticket("ORD", "NONE")
        ticket_9 = Ticket("SLC", "PIT")
        ticket_10 = Ticket("BHM", "FLG")

        tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

expected output: ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP", "SLC", "PIT", "ORD", "NONE"]

'''

#Your solution should run in linear time. You can assume that your
# function will always be handed a valid ticket chain as input. 

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    our_dict = {}

    #construct dict

    for ticket in tickets:
        our_dict[ticket.source] = ticket.destination #origin = key = value dest

    # print(our_dict)

    route = []
    route.append(our_dict['NONE']) #this adds the first dest (add the value LAX)
    last = our_dict['NONE'] #this adds LAX to last

    while our_dict[last] != 'NONE': #while the destination is None, keep looping
        #use the value of last item, to be key of the next item
        route.append(our_dict[last]) #this has added SFO
        next_key = our_dict[last]
        last = our_dict[next_key] #this now contains BHM
        route.append(last)
        # print(f'last is now {last}')

    # route.append('NONE')
    print(route)


    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]


# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
reconstruct_trip(tickets, 3)
