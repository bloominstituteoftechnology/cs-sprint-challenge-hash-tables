def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    nums = {}
    result = []

    for arr in arrays:
        for i in range(len(arr)):
            if arr[i] in nums:
                nums[arr[i]] += 1

                if nums[arr[i]] == len(arrays):
                    result.append(arr[i])

            else:
                nums[arr[i]] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
