def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    result = []
    for num in a:
        if d.get(abs(num)):
            result.append(abs(num))
        else:
            d[abs(num)] = num


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
"""
line 5: dictionary holds all numbers in a 
line 6: array to return matches in absolute value(result)
line 7: if the num has a corresponding number in dictionary
line 8: .get method returns the value for the givin key
line 9: adding results to the list
line 10: if no value is found pass num a new key along with its value
"""