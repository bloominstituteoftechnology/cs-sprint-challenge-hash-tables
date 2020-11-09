def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    did_have_duplicates = False
    results_dict = {}
    weights_copy = []
    if len(weights) == 1:
        return None
    
    for weight in weights:
        if results_dict.get(weight, '00') != '00':
            print("")
            results_dict[weight].append(weights.index(weight))
            did_have_duplicates = True
        else:
            # results_dict[weight] = weights.index(weight)
            results_dict[weight] = [weights.index(weight)]
        
        weights_copy.append(weight)    
        weights[weights.index(weight)] = None
    
    x = None
    x_num = None
    y = None
    y_num = None
    arrayay = [None] * 2
    for weight in weights_copy:
        if arrayay[0] != None and arrayay[1] != None:
            break
        if did_have_duplicates:
            calculation = limit - weight
            if results_dict.get(calculation, '00') != '00':
                if len(results_dict[calculation]) > 1:
                    print("booty ho")
                
                if x == None:
                    x = results_dict[calculation][0]
                    x_num = calculation
                else:
                    y = results_dict[calculation][1]
                    y_num = calculation
            else:
                print("Not")
            
            if x == None or y == None:
                print("continue")
            else:
                if x_num > y_num:
                    arrayay[0] = x
                    arrayay[1] = y
                else:
                    arrayay[0] = y
                    arrayay[1] = x
                
            
        else:
            calculation = limit - weight
            if results_dict.get(calculation, '00') != '00':
                if x == None:
                    x = results_dict[calculation][0]
                    x_num = calculation
                else:
                    y = results_dict[calculation][0]
                    y_num = calculation
            else:
                print("Not")
            
            if x == None or y == None:
                print("continue")
            else:
                if x_num > y_num:
                    arrayay[0] = x
                    arrayay[1] = y
                else:
                    arrayay[0] = y
                    arrayay[1] = x

    
    # return the largest index first like [3,1]
    return arrayay

get_indices_of_item_weights([9], 1, 9)