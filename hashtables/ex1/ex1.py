def get_indices_of_item_weights(weights, length, limit):
 # create a dictionary to cache items 
    cache = {}
    for i, weight in enumerate(weights):
        cache[weight] = i
  #iterating through table checking weights that meet limit
    for i, weight in enumerate(weights):
        if limit - weight in cache:
              j = cache[limit - weight]
              if i > j:
                  return (i, j)
              else:
                    return (j, i)
    return None
            
   
   
        
        

    
      
        
 
 
