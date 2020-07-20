import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #set hash table
    hash_table = {}
    
    #set result array
    results = []
    
    for num in a:
        absolute_value = abs(num)
        
        if hash_table.get(absolute_value) is not None:
            results.append(absolute_value)
        
        else:
            hash_table[absolute_value] = absolute_value

    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
