def intersection(arrays):
    """
    YOUR CODE HERE
    """
    numbers = dict()
    count = 0

    for array in arrays:
        count += 1
        
        for num in array:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

    result = list()
    numbers_list = numbers.items()

    for number in numbers_list:
        if number[1] == count:
            result.append(number[0])

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
