def has_negatives(a):
    numbers = a
    
    # positives = {}
    # # non_positives = {}
    # retval = []
    
    # for n in numbers:
    #     if n > 0:
    #         positives[n] = n
            
    #     else:
    #         non_positives[n] = n
            
    # for p in positives:
    #     if -p in non_positives:
    #         retval.append(p)



    ht = {}
    for n in numbers:
        if n > 0:
           ht[n] = 'positive'

    for n in numbers:
        if n < 0 and -n in ht:
            ht[-n] = 'both'
    
    return [key for (key,value) in ht.items() if value == 'both']
        

            

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))