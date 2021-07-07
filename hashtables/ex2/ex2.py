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
    # goal is to return a list of the entire trip, in the order of source to desination
    #the first and the last tickets will be the base case 
    # first ticket will not have a source before it, last ticket will not have a destination 
    trip = []
    trip_trakcer = {}


    for ticket in tickets:
        #create conditional to find first and last tickets 
        if ticket.source is "NONE":
            #this is our first ticket:
            first_ticket = ticket.destination
        elif ticket.destination is "NONE":
            last_ticket = ticket.source
        # add the sources and destinations to the trip_tracker dictionary
        trip_trakcer[ticket.source] = ticket.destination
    
    print("THIS IS DICTIONARY", trip_trakcer)
            
    for i in range(length):
        #conditional checking 
        print("THIS IS I", i)
        if i == 0:
            #this is the start of the trip
            trip.append(first_ticket)
            current_area = first_ticket

            
        
        elif i == length:
            #this is the end of the trip
            trip.append(last_ticket)
        else:
            #move the trips from the trip_trakcer dictionary into the trip list
            # create a variable to point the destinaiton of the current trip which will be the source of the next flight
            dest_to_become_source = current_area 
            #check if the dest to become source is in the dicitonary 
            if dest_to_become_source in trip_trakcer:
                trip.append(trip_trakcer[dest_to_become_source])
                current_area = trip_trakcer[dest_to_become_source]
            

       

 

        
        
        
        # print("TICKET SOURCE:", ticket.source, "TICKET DESTINATION:", ticket.destination)
    
    return trip
