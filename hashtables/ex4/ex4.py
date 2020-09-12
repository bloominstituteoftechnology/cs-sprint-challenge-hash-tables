def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_hash = {}
    result = []

    for num in a:
        if num * -1 in num_hash:
            if num < 0:
                result.append((num * -1))
            else:
                result.append(num)

        else:
            num_hash[num] = 1 

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
