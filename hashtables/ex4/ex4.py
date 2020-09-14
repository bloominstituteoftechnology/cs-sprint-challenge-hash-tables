def has_negatives(arr):
    # create a dict with a key for the original number
    # and a value for the count of corresponding negatives
    cache_list = [1]*len(arr)
    # actual cache is now housing the list values
    # as keys in a dictionary
    actual_cache = dict(zip(arr, cache_list))
    # next step is to check the dict to see if there are
    # any positives that have a negative somewhere in the list
    hasNegatives = []
    # store resulting values in this list
    for key in actual_cache:
        # if the key is greater than 0 it can have a corresponding negative
        if key > 0:
            try:
                # if we can access both the key and the key as a negative
                # then we know to append that key to the results list
                if actual_cache[key] is not None and actual_cache[-key] is not None:
                    hasNegatives.append(key)
            # if this doesn't apply to the key we are iterating through then
            # pass and keep iterating through the keys
            except:
                pass
    return hasNegatives

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))