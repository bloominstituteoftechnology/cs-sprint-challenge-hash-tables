def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    positive_numbers = []

    for number in a:

        # add all numbers to the dictionary
        dictionary[number] = 1

        # if the current number's additive inverse in the dictionary, add the positive version to the resulting array
        # no zero
        if number is not 0 and number * -1 in dictionary:
            positive_numbers.append(abs(number))

    return positive_numbers


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
