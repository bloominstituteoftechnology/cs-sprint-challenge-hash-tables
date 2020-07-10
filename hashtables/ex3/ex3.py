def intersection(arrays):
    """
    Time complexity O(n) where n is the total count of numbers in all lists
    """
    if len(arrays) == 0:
        return []
    counts = {}
    for nums in arrays:
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
    return [num for (num, count) in counts.items() if count == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
