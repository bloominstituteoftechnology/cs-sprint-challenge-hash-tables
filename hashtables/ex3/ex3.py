def intersection(arrays):
    """
    YOUR CODE HERE
    """
    common_nums = {}

    for list in arrays:
        for number in list:
            if number in common_nums:
                common_nums[number] += 1
            else:
                common_nums[number] = 1
    
    result = [item[0] for item in common_nums.items() if item[1] == len(arrays)]        

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
