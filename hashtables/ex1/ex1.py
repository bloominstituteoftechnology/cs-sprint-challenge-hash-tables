def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Searching for two items whose sum of weights equals the weight limit
    # mapping of indicing to numbers 
    # when we need to make a mapping that doesn't exist for me I need to make a hashtable
    weights_dict = {}

     # if the length of the weights is less than 1, we cannot return two indices, return None

    if len(weights) <= 1:
            return None

    for i in range(len(weights)):
        # assign a variable to the index value for each loop index in weights
        curr = weights[i]
        #calculate the difference between the limit and the current index value
        difference = limit - curr
        print("DIFFERENCE", difference)
        # create a conditional checking if the difference is in the weights_dictionary
        if difference in weights_dict:
            #if it is in the weights_dictionary, return the loop index, and the index of the difference value 
            print("RETURNING", (i, weights_dict[difference]))
            return (i, weights_dict[difference])
        else:
            # if it is not in the dictionary, assign the value of the current index to the index loop
           weights_dict[curr] = i  
        
   
   
      
  
