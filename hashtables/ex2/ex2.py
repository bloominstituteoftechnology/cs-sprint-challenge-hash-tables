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
    hash_table = {}

    route = [None] * length
    current_target = 'NONE'
    current_index = 0

    for i in range(length):
        # Add the source and the destination to the hash
        hash_table[tickets[i].source] = tickets[i].destination
        
        # Store the next destination in the route and change the current target
        if tickets[i].source == current_target:
            current_target = tickets[i].destination
            route[current_index] = current_target
            # Exit if final destination is reached
            if current_target == 'NONE':
                break
            current_index += 1

            # Search current entries for the next destination
            while current_target in hash_table:
                current_target = hash_table[current_target]
                route[current_index] = current_target
                # Exit if final destination is reached
                if current_target == 'NONE':
                    break
                current_index += 1


    return route
