def intersection(arrays):
    """
    YOUR CODE HERE
    """
    numbers = {}

    for arr in range(len(arrays)):
        results = []

        for num in arrays[arr]:
            if arr == 0:
                numbers[num] = 1

            elif arr == (len(arrays) - 1):
                if num in numbers:
                    results.append(num)
            
            else:
                if num in numbers:
                    numbers[num] += 1
    


    return results


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
