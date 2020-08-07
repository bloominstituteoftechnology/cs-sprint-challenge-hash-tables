cache = {}
def has_negatives(arr):
    results = []
    for i in range(len(arr)):
        #if > 0 put into cache
        if (arr[i] > 0):
            cache[arr[i]] = arr[i]
    
 
    
    for i in range(len(arr)):
        if -arr[i] > 0:
            #if less than zero search cache
            if -arr[i] in cache:
                #if found add to array
                results.append(-arr[i])
        
    
    return results
arr = [-1,-2,1,2,3,4,-4]
print(has_negatives(arr))

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
