from functools import reduce
# from hashtable import HashTable


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = list(reduce(lambda i, j: i & j, (set(x) for x in arrays)))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
