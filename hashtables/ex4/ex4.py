def has_negatives(a):

    # create empty dict
    d = {}

    # for item in a
    for index, value in enumerate(a):
    
        # add all items to a dictionary
        d[index] = value

    # empty list
    positive_numbers = []

    pos_has_neg = []

    # # for key in dict
    for key, value in d.items():

        if value < 1:

            print('less than 1', value)

            if -value in d:
                if -value != 0:
                    pos_has_neg.append(-value)

    return pos_has_neg

    # for key, value in d.items():
        
    #     # for num in positive_numbers:

    #     #     if -num == value:

    #     if -value in d:

    #             pos_has_neg.append(-value)

    # return pos_has_neg    



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


    print(has_negatives([1,2,3]))

    a = list(range(5000))
    a += [-1,-2,-3]

    print(has_negatives(a))