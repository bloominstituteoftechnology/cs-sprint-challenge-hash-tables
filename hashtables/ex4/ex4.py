def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    numbers = {}

    for number in a:
        abs_number = abs(number)
        if abs_number not in numbers:
            numbers[abs_number] == number
        else:
            result.append(abs_number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
