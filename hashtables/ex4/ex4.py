def has_negatives(a):
    negative_nums = {}

    for num in a:
        negative_nums[num] = -num
    
    result = []

    for num in negative_nums.keys():
        if num > 0 and negative_nums[num] in negative_nums:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
