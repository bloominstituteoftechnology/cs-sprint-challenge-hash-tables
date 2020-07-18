def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    number_counts = {}

    length = len(arrays)
    for array in arrays:
        for number in array:
            if number not in number_counts:
                number_counts[number] = 1
            else:
                number_counts[number] += 1
                if number_counts[number] == length:
                    result.append(number)
    '''for number in arrays[0]:
        count = 1
        for i in range(1, length):
            if number in arrays[i]:
                count += 1
                if count == length:
                    result.append(number)'''

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
