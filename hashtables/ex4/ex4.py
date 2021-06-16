def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    d = {}

    for n in a:
        if n in d:
            continue
        else:
            d[n] = 1

    result = []

    for n in d:
        # if abs(n) in result:
        #     continue 
        if -n in d:
            if n == 0:
                continue 
            if abs(n) not in result:
                result.append(abs(n))

    return result

a = list(range(5000000))
a += [-1,-2,-3]

print(has_negatives(a))


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
