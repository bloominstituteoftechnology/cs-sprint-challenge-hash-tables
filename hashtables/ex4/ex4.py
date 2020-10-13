def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # anom func
    a.sort(key=lambda x: x + 0.5 if x >= 0 else -x)
    # collection of pairs 
    pairs_ = []

    # Return a zip object whose .__next__() method returns a tuple where the i-th element comes from the i-th iterable argument. 
    for pair in [(x, y) for x, y in zip(a, a[1:]) if x == -y]:
        # append each pair 
        pairs_.extend(pair)
        
    # append pos nums only 
    result = []
    for num in pairs_:
        if num >= 0:
            result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
