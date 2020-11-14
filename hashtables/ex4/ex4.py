def has_negatives(a):
    # WE'VE GOTTA HAVE A CACHE, RIGHT?
    cache = {}
    # WE'VE GOTTA HAVE A RESULT ARRAY, EH?
    result = []
    # WHY DON'T WE ADD THE ABSOLUTE VALUES OF ALL...
    # ...THE NEGATIVE NUMBERS INTO THE CACHE?
    for value in a:
        if value < 0:
            cache[abs(value)] = True
    # WE CAN NOW COMPARE THE VALUES IN THE INPUT...
    # ...ARRAY AGAINST THE VALUES IN THE CACHE, NO?
    for value in a:
        if value in cache:
            # IF A VALUE APPEARS IN BOTH THE INPUT...
            # ...ARRAY AND THE CACHE, WHY NOT APPEND...
            # ...THAT TO THE RESULTS ARRAY?
            result.append(value)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
