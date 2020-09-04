def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

cache = {}

for i in range(len(weights)):
        cache[weights[i]] = i
for i in range(len(weights)):
        lw = limit - weights[i]
        if lw in cache:
            return (max(i, cache[lw]), min(i, cache[lw]))
