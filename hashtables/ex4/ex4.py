def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dic = {}
    result = []
    
    for num in a:
        dic[num] = 1
        if num != 0 and -num in dic:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
