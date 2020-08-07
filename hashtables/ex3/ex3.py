def intersection(arrays):
    dict = {}
    result = []

    # set value_count as the key (i.e. the value we are looking for) and track the number of times it appears
    # confusing i know - but it makes sense in my head
    for keys in arrays:
        for value_count in keys:
            if value_count in dict:
                # track the number of items our value has appeared
                dict[value_count] += 1
            else:
                # if the value the value is not in the dict we count it as a first occurance
                dict[value_count] = 1
            # if our value matches the number of arrays
            # we know it appears in each array and intersects
            if dict[value_count] == len(arrays):
                result.append(value_count)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
