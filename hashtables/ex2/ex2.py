#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = {}
    organize_routes = {}
    destinations_array = []
    # loop through array of tickets
    for i in range(length):
        # add starting airport as key and destination as value
        route[tickets[i].source] = tickets[i].destination
        
        # destional has to equal source
        # So I need to somehow find the starting airport that equals none and its destination. Then that destinations needs to equal another tickets starting and so on. 
    starting = 'NONE'
    for key, value in dict.items():
        # find key that equals none 
        # print (key, value)
        if starting in key:
            # starting becomes the value
            starting = value
            organize_routes[key] = value
            # restart search
            
            print(f'\nThe new starting airport is {starting}')
        # push destination to array
        # destinations_array.append(tickets[i].destination)
    print(organize_routes)
    return destinations_array

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


#  expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP", "SLC", "PIT", "ORD", "NONE"]


print(reconstruct_trip(tickets, 10))

