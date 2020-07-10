def has_negatives(a):
    """
    For an input list of integers, we wish to know which positive numbers
    have corresponding negative numbers in the list.

    Example input:

    ```python
    [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
    ```

    Input can be in any order.

    Example return value:

    [ 1, 3, 4 ]
    """
    result = []
    cache = {}
    for x in a:
        cache[x] = x

    for x in a:
        if -x in cache:
            if abs(x) not in result and x > 0:
                result.append(abs(x))

    return result


if __name__ == "__main__":
    a = list(range(5000000))
    a += [-1,-2,-3]
    print(has_negatives(a))
