#ex1.py



def get_indices_of_item_weights(weights, length, limit):
  
    cache = {}
    
    # Check list of weights by index

    for i in range(length):

        # Store each weight as a key

        weight = weights[i]

        #print(f'key and value:{i, weight}')
        if weight in cache:

            # Store the weight index as the value

            value = cache[weight]

            # Return tuple

            return(i, value)
            
        
        # Calculate the difference

        difference = limit - weight

        # Add to cache

        cache[difference] = i
        #print(difference)

    return None


if __name__ == "__main__":
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
    