def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    dict = {}
    results = []
    for n in a: 
        dict[n] = True
    for n in a: 
        if n > 0 and -n in dict: 
            results.append(n)
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
