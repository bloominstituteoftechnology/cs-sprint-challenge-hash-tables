def has_negatives(a):
    """
    For an input list of integers, we wish to know which numbers appear in both
    positive and negative forms.
    """

    # Intialize a dictionary to track integers seen.
    # Key: abs(integer)
    # Value: (positive_seen, negative_seen)
    lookup = {}

    # Read through the full list of integers, updating the dictionary along the
    # way.
    for num in a:
        if num > 0:
            if num not in lookup:
                # First encounter with abs(num), num positive.
                lookup[num] = [True, False]
            else:
                # Second or greater encounter with abs(num), num positive.
                lookup[num][0] = True
        elif num < 0:
            if abs(num) not in lookup:
                # First encounter with abs(num), num negative.
                lookup[abs(num)] = [False, True]
            else:
                # Second or greater encounter with abs(num), num negative.
                lookup[abs(num)][1] = True

    # Return absolute value of integers encountered as both positives and
    # negatives.
    return [key for (key, value) in lookup.items() if value == [True, True]]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
