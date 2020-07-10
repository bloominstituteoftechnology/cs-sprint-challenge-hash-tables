def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create storage
    # loop over
    # insert all values in dict

    array_storage = {}

    array_count = 0

    first_array = []

    num_storage = {}

    intersections = []

    for idx, array in enumerate(arrays):
        array_storage[idx] = array
        array_count += 1

        # first_array = array_storage[0]

        if idx <= (len(arrays) - 1):
            first_array.extend(array_storage[idx])

    for num in first_array:

        if num not in num_storage:
            num_storage[num] = 1
        else:
            num_storage[num] += 1
            # print(num_storage[num])

        if num_storage[num] == array_count:
            #print(f"num_value: {num_storage[num]}, {array_count}")
            intersections.append(num)
            #print(num, "num")

    # print(intersections)

    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
