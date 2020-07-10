def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    o = dict()
    for i in arrays:
        for j in i:
            if j in o:
                o[j] += 1
            else:
                o[j] = 1
    #Add them up
    result = [data[0] for data in o.items() if data[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
