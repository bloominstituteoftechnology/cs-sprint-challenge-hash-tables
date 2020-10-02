def has_negatives(a):
 # create a dictionary
    cache = {}
    
    #create seperate lists
    results = []
  
    for num in a:
        if num != 0:
           cache[num] = 1
        if -num in cache:
            results.append(abs(num))

            

     
 
 
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
