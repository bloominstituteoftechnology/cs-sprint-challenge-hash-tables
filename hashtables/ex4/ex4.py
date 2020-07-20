def has_negatives(a):
    # Create a cache
    cache = {}
    # Create a results arr
    res = []

    # Traverse the input arr
    for val in a:
        # Check if the additive inverse val is in the cache
        if -val in cache:
            # If true, add the absolute value to the res arr
            res.append(abs(val))
        # If it's not in the cache, add it
        else:
            cache[val] = True

    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
