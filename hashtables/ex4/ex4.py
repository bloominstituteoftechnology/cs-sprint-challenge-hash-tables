def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    numbers = {}

    for number in a:
        # Get absolute number
        abs_number = abs(number)
        # Check if number already in dict or not
        if abs_number not in numbers:
            # Save new number in dict
            numbers[abs_number] = number
        else:
            # Add number to result
            result.append(abs_number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
