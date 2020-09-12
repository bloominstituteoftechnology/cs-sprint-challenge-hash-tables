def get_indices_of_item_weights(weights, length, limit):
    
    # create empty hashtable
    d = {}

    # enumerate weight list
    for index, value in enumerate(weights):

        # if hashtable contains an entry for the weight limit - the current weight value 
        if limit - value in d:

            # get the index of that second value
            pair = d.get(limit-value), index
            return tuple(sorted(pair, reverse=True))

        # if not in hashtable
        else:

            # create entry
            d[value] = index

    return None





weights_2 = [4, 4]

print((get_indices_of_item_weights(weights_2, 2, 8)))

# store weight's list index as value

# empty hashtable
# for index, value in enumerate(weights_2):
    # if limit - value in hashtable:
        # second_value = limit - value
        # return sorted tuple (value, second_value)
    # else:
        # hashtable[value] = index