# Find the intersection of all numbers inside each subarray
# in the arrays input

# Loop through each subarray and add each number to the cache
# if it already exists in the cache then add it to the results array

# The output should be a list [] of all numbers that exist in each of
# the subarrays


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []

    cache = {}

    for subs in arrays:
        for num in subs:
            if num not in cache:
                cache[num] = 1
            else:
                result.append(num)

    print(result)
    result = dict.fromkeys(result)
    print(result)
    result = list(result)
    print(result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
