def has_negatives(a):
    result = []
    my_dict = {}
            
    # loop though list
    for i in a:
        my_dict[i] = i
        # if num in not 0 or in dictionary
        if i != 0 and -i in my_dict:
            # return num as positive number
            result.append(abs(i))
                
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
