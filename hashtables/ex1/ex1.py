def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    Plan
    ----
    1. create an empty list
    2. loop through weight array from the first item
        loop through weigh array again begin from second item
        check if sum of the first item is equal to sum of second item
        add the two index in the empty list
    3. change list to tuple
    """
    # Your code here
    ans = []
    if len(weights) < 2:
        return None
    for i in range(0, len(weights) - 1):
        for j in range(1, len(weights) - 1):
            # print(limit)
            if (weights[i]+ weights[j]) == limit:
                ans.append(i)
                ans.append(j)
            break    
    return ans
print(get_indices_of_item_weights([4, 6, 10, 15, 16],5,21))

