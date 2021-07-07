# Merging Two Packages
#
# Given a package with a weight limit (limit) 
# and a list (weights) of item weights, 
# implement a function (get_indices_of_item_weights) 
# that finds two items 
# whose sum of weights equals the weight limit (limit). 
#
# Your function will return a tuple of integers that has the following form: 
# (zero, one)
#
# The higher valued index should be placed in the zeroth index 
# The smaller index should be placed in the first index
#
# Should run as O(N)


def get_indices_of_item_weights(weights, length, limit):
    """
    weights: list of integers 
    length: length of weights list
    limit: weight limit value

    Returns tuple of indices of weight values which sum to limit
    """
    # create cache
    cache = {}

    # fail if input array is shorter than 2 entries (test case 1)
    if length <= 1:
        print("Error: List too short.")
        return None

    for i in range(length):
        current = weights[i]
         # check if the current weight is in the cache
         # aka the matching/previously inserted weight index = the value in the cache
        if current in cache:
            # prev weight index = value, so get index of prev
            previous = cache[current]
            # print(cache)
            return (i, previous)
        # now the hash table/cache key is the smaller weight needed to reach limit
        # aka that value is the current weight's index
        cache[limit - weights[i]] = i

    return None


# test should ouput [3,1]
weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))