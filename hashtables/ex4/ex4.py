import math
def has_negatives(a):
    # Initialize dictionary for storage
    dictionary = {}
    result = []
    
    # Loop through the input array
    for item in a:
        # check if absolute of item is not in dictionary
        if int(math.fabs(item)) not in dictionary:
            # add the value to dictionary
            dictionary[int(math.fabs(item))] = 1
        else:
            # value exists, so increment count in dictionary
            dictionary[int(math.fabs(item))] += 1
            
    # Loop through elements in dictionary
    for item in dictionary:
        # check the item count
        if dictionary[item] > 1:
            # add item with count greater than 1 to result list
            result.append(item)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
