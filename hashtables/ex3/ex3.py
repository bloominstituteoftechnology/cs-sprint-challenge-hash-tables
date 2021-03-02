from collections import Counter 
  
# def commonElement(ar1,ar2,ar3): 
#      # first convert lists into dictionary 
#      ar1 = Counter(ar1) 
#      ar2 = Counter(ar2) 
#      ar3 = Counter(ar3) 
     
#      # perform intersection operation 
#      resultDict = dict(ar1.items() & ar2.items() & ar3.items()) 
#      common = [] 
      
#      # iterate through resultant dictionary 
#      # and collect common elements 
#      for (key,val) in resultDict.items(): 
#           for i in range(0,val): 
#                common.append(key) 
  
#      print(common) 


def intersection(arrays):

    if len(arrays)==1: 
        return arrays[0] 
    else: 
        return arrays[0].intersection(recursively(arrays[1:])) 
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
