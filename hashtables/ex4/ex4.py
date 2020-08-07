def has_negatives(a):
    """
    Prompt: For an input list of integers, we wish to know which
    positive numbers have corresponding negative numbers in the list.

    Example input:
    a = [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]

    Example return value:
    [ 1, 3, 4 ]
    Because 1, 3, and 4 are the positive numbers that have corresponding
    negative numbers in the list.

    Return value can be in any order.
    Solve this problem with a hash table.

    Limits:
    The input list can contain approximately 5,000,000 elements.
    """
    # Initialize hash table and final array
    cache = {}
    result = []
    # For each number in the list
    for number in a:
        # If that number isn't in the hash table
        if number not in cache:
            # that spot in the hash table will become that value but with the opposite sign
            cache[number] = number*-1
            # If that number is in the cache and the number isn't 0
            if cache[number] in cache and number != 0:
                # Add the absolute value of that number to the final array
                result.append(abs(cache[number]))
    # Return the final array
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
