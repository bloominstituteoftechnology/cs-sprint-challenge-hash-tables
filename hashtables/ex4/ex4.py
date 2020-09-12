def has_negatives(a):
    """
    YOUR CODE HERE
    """
    pos = {}
    neg = {}
    result = []
    # Your code here
    for i in a:
        if i <0:
            neg[i]=i* -1
            
        elif i >0:
           pos[i] =i
           
    print(pos, neg)  
    
    for i in neg.values():
        if i in pos:
            result.append(i) 
             
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
