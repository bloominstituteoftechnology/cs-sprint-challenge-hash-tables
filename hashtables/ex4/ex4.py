def has_negatives(a):

    dict = {}
    result = []

    for value in a:
        # check if opposite integer/num is in the array
        if -value in dict:
            # if it exists in the dictionary append it to the results array
            # append the number
            result.append(value if value >= 0 else -value)
        # add all numbers to the dict
        dict[value] = value

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
