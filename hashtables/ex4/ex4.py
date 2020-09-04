def has_negatives(a):
    """
    YOUR CODE HERE
    """
    table = {}
    for i in a:
        if i > 0:
            table[i] = 0
    
    for i in a:
        if i < 0:
            try:
                table[abs(i)] = 1
            except:
                pass
    
    result = [i for i in table if table[i]>0]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
