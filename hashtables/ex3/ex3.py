def intersection(arrays):
    count = {}
    
    for arr in arrays:
        # separate hash table to keep track of numbers seen in each array,
        # to avoid counting multiple occurrences of same number
        seen = {}
        for num in arr:
            if num in seen:
                continue
            elif num in count:
                count[num] += 1
            else:
                count[num] = 1
            seen[num] = True
    
    result = []
    for num in count:
        if count[num] == len(arrays):
            result.append(num)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
