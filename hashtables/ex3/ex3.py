def intersection(arrays):
    """
    Finds the intersection of multiple lists of integers, wihtout using numpy
    or sets.
    """

    # Create a dictionary to track the count of how many lists a given integer
    # appears in.
    counts = {}

    for array in arrays:
        # Use a second dictionary to track integers already seen (and therefore
        # counted) in the current list.
        in_this = {}

        for num in array:
            if num in in_this:
                # Nothing needs to be done for repeat occurrences of a number
                # in a single list.
                pass
            else:
                # For the first appearance of each number, however, we need to
                # mark it as seen in the current list and increment the count
                # of lists in which it appears.
                in_this[num] = True

                if num in counts:
                    counts[num] += 1
                else:
                    counts[num] = 1

    # Integers which in appear in a number of lists equal to the total number
    # must logically appear in all lists given.
    return [key for (key, value) in counts.items() if value == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
