def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # anom func to sort through 
    a.sort(key=lambda x: x + 0.5 if x >= 0 else -x)
    # collection of pairs 
    pairs_ = []
    
#   enumerate pairs of consecutive list entries.
    for pair in [(x, y) for x, y in zip(a, a[1:]) if x == -y]:
        # append each pair int
        pairs_.extend(pair)
        
    # append pos nums only 
    result = []
    for num in pairs_:
        if num >= 0:
            result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
