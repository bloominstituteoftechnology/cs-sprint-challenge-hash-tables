def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = set()
    result = []
    
    for entry in a:
        if entry < 0 and entry not in table:
            table.add(entry)

    for entry in a:       
        if -(entry) in table:
            result.append(entry)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
