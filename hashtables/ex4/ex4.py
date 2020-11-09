def has_negatives(a):
    """
    Understand:
    Test File

    Plan:
    sets would be wonderful here
    since we cant use a set a dictionary will do.
    put values into a list and compare to see if it has value needed.
    """

    dict = {}
    result = []

    for num in a:
        if num > 0:
            dict[num] = num

    result = [abs(num) for num in a if num * -1 in dict]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
