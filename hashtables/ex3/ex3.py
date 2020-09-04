def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dict_vals = {}
    for i in arrays:
        for j in i:
            if j in dict_vals:
                dict_vals[j] += 1
            else:
                dict_vals[j] = 1
    output_array = [k for (k,v) in dict_vals.items() if v == len(arrays)]

    return output_array


if __name__ == "__main__":
    arrays = []


    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
