def has_negatives(arr):
    # build hashtable and result arr
    ht = {}
    result = []

    # loop over arr
    for num in arr:

        # establish a negative val for each number we're looking at
        negative = num * -1

        # check to see if the negative val is already in the hashtable
        if negative in ht:

            # if so, push the absolute value onto the result arr
            result.append(max(num, negative))

        # otherwise add the num and negative as a key/value pair
        else:
            ht[num] = negative

    return result


if __name__ == "__main__":
    print(has_negatives([-1, 1, -1, -4, -2, 1, 2, 3, 4, -4, -4, -7, 7]))
