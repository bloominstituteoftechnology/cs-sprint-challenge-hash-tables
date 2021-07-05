def intersection(arrays):
    """
    Finds the intersection of the input lists of numbers.
    """
    # Create hash table (dict) to store numbers in for faster O(1) lookup (for 
    # any individual lookup):
    # numbers = {}

    # Create list for intersection of the sets:
    # intersection = []

    # Populate hash table with numbers from the first list (keys), because any numbers 
    # not in the first list will not be in the intersection of the lists, by definition.
    numbers = {item:False for item in arrays[0]}
    # Now check the other input lists in order, removing any number/item that is not in both:
    for list in arrays[1:]:
        for item in list:  # NOT actually O(n**2); just O(n) for the whole input matrix.
            # Mark as True to flag any items that are in the intersection of the two lists:
            if item in numbers:
                numbers[item] = True
        # Keep only the numbers that are in the intersection of the two lists:
        numbers = {key:value for key, value in numbers.items() if value == True}
        # Mark all as False again to start a fresh comparison with the next list:
        for item in numbers:
            numbers[item] = False

    return [*numbers.keys()]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000001)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000001)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
