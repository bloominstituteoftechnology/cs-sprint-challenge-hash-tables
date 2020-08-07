def has_negatives(a):
    # Your code here
    negatives = {}
    result = []

    for num in a:
        if num < 0:
            negatives[abs(num)] = num
    
    for num in a:
        if num in negatives:
            result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
