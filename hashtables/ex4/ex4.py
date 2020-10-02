def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = [] # result list
    my_dict = {} #setting up hash table dict

    # for loop to loop thru the list 
    for pos_num in a: 
        my_dict[pos_num] = pos_num # setting up pos_num int in my dictionary

        if pos_num != 0 and - pos_num in my_dict: #if number not 0 or in dictionary 
            result.append(abs(pos_num)) #return number as positive number by appending
# return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
