def get_indices_of_item_weights(weights, length, limit):
    # Your code here

    # dict of all possible weight pair options
    weights_dict = {}

    # build up dict of all possible weight pair options based on the the input
    for i in weights:
        if i not in weights_dict:
            weights_dict[i] = i
    
    # create an array to hold solution pair(s)
    output = []

    # for each of the possible weight options, check to see if there is a matching pair found by the max limit minus it's weight
    for i in range(length):
        cur = weights[i]
        pair = limit - cur

        # if there is a matching pair, append it to the cur in the output
        if pair in weights_dict:
            output.append(i)
    
    # return output of pairing(s), sort by highest value at index zeroth
    if len(output) == 2:
        # print(sorted(output, reverse=True))
        return sorted(output, reverse = True)
    
    # base case, no output to return
    else:
        return None