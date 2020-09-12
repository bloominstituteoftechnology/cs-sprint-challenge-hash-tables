def intersection(arrays):
    my_dict = {}
    result = []

    # for index in len(arrays):
    #     array = arrays[index]
    #     my_dict[index] = array
    #     for 

    for array in arrays:
        for element in array:
            if element not in my_dict:
                my_dict[element] = 1
            else:
                my_dict[element] += 1

            if my_dict[element] == len(arrays):
                result.append(element)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
