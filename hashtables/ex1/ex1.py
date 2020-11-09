def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    for i in range(length):
        if weights[i] in dictionary:
            dictionary[weights[i]] = [dictionary[weights[i]], i]
        else:
            dictionary[weights[i]] = i
    for key in dictionary:
        remainder = limit-key
        if remainder in dictionary:
            if type(dictionary[remainder]) is list:
                return [max(dictionary[key]), min(dictionary[key])]
            else:
                if dictionary[key] > dictionary[remainder]:
                    return [dictionary[key], dictionary[remainder]]
                else:
                    return [dictionary[remainder], dictionary[key]]
    return None


print(get_indices_of_item_weights([4, 4], 2, 8))
