# For each number in the input array, add it to the cache

# For positive integers, multiply each number by -1 and check
# if it is already in the cache...if it is in the cache
# that means its positive value is also in the cache so append it
# to the results list


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    result = []

    for num in a:
        if num not in cache:
            cache[num] = 1

    for num in a:
        if (num * -1) in cache and num > 0:
            result.append(num)

    print(result)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
