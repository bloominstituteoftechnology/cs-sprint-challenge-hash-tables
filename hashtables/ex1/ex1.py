def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    arr = []

    for w in weights:
        # setting weight value
        if w not in d.keys():
            d[w] = weights.index(w)

    for w in weights:
        result = limit - w
        # checking results
        if result in d.keys():
            arr.append(d[w])

    # are arrays equal?
    if len(arr) == 2:
        if arr[0] == arr[1]:
            arr[1] = weights.index(weights[arr[1]], weights.index(weights[arr[1]])+1)
        
        arr.sort(reverse=True)
        return tuple(arr)

    return None