def intersection(arrays):

    my_dict = {}

    for array in arrays:
        for num in array:
            value = my_dict.get(num)
            if value is None:
                my_dict[num] = 1
            else:
                my_dict[num] = value + 1
            
    length = len(arrays)
    result = []

    for num in my_dict.keys():
        value = my_dict[num]
        if value == length:
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
