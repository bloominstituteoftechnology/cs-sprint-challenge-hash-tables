def intersection(arrays):

    num_arrays = len(arrays)
    dict = {}

    for array in arrays:
        for i in array:
            if i in dict:

            else:
                dict[i] = array.count(i)


    # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
