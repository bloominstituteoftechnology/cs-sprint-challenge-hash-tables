def has_negatives(a):
    """
    YOUR CODE HERE
    """

    #scan from left to right. place first occurrences of each element if it's absolute value does not exist
    first_occurrences = {}
    output_list = []

    for i in a:
        if abs(i) not in first_occurrences:
            if i != 0:
                first_occurrences[abs(i)] = i/abs(i)
        elif i < 0 and first_occurrences[abs(i)] > 0:
                output_list.append(abs(i))
        elif i > 0 and first_occurrences[abs(i)] < 0:
                output_list.append(abs(i))
        else: # when i = 0
            continue

    return output_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
