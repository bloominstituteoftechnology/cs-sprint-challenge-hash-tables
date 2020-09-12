def get_indices_of_item_weights(weights, length, limit):
    """
    A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. How can we use a hash table in order to implement a solution with a better runtime?

Think about what we can store in the hash table in order to help us to solve this problem more efficiently.

What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key?

If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for limit - weight. If it does, then we've found the two items whose weights sum up to the limit!


    """
    cache = {}

    if length <= 1:
        return None
    for index in range(length):
        weight = weights[index]

        if weight in cache:
            value = cache[weight]
            return (index, value)

        difference = limit - weight
        cache[difference] = index

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

