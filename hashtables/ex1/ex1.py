def get_indices_of_item_weights(weights, length, limit):
    
    # no point if the weight is over the limit
    # weights =  [w for w in weights if w < limit]

    ht = {}

    # make hashtable for lookup

    i = -1
    for w in weights:
        i += 1
        ht[w] = i

    # lookup first item
    for w1 in weights:
        # print(w1)
        if w1 in ht:
            # print('here')
            w2 = limit - w1
            # print(w2)
            if w2 == w1: #dupes, need two instances from weights
                # print('here')
                occurrences = [i for i, j in enumerate(weights) if j == w1]
                print(occurrences)
                
                # Are there are at least two instances of the w1 / w2 in weights?
                if len(occurrences) > 1:
                    retval = (occurrences[1], occurrences[0])
                    # print(retval[1])
                    return (occurrences[1], occurrences[0])
                    
            # weights are not duplicates
            if w2 in ht: # found both, so both must be in weights
                index1 = weights.index(w1)
                index2 = weights.index(w2)
                if index1 > index2:
                    return (index1, index2)
                else:
                    return (index2, index1)
    # Tried every combo
    return None
        
        

            


weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2[0])

