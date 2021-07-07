def intersection(arrays):
    """
    Time complexity is O(2n) worst case (ones to make table, once for all 
    inputs are dupes) round to O(n).
    Space complexity is O(n). table will get larger by unique values and 
    proportionally results will get smaller
    """
    # Your code here
    table = {}

    for arr in arrays:
        for ele in arr:
            table[ele] = table.get(ele, 0) + 1

    result = []

    for key in table:
        if table[key] > 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
