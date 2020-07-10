def get_indices_of_item_weights(weights, length, limit):

    # length is not required as a parameter
    
    # no point if the weight is over the limit
    reasonable =  [w for w in weights if w < limit]
    
    # Crazy python
    reasonable.sort()
    
    # for any weight, what is the exact matching weight (dict)
    matches = {}
    
    # linear, build checking table
    for el in reasonable:
        matches[el] = limit - el
        
    # linear, check
    for r in reasonable:
        if r in matches:
#             return (max(m, matches[m]), min(m, matches[m])
#                     
#     return None
        pass
        
foo = get_indices_of_item_weights([1,700, 1, 2,3, 5000], 3, 4000)

foo