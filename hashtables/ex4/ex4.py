def has_negatives(a):
    dict = {}
    a.sort()
    for num in a:
        entry = {num:a.index(num)}
        dict.update(entry)
    result = []
    for i in dict.keys():
        if i > 0 and i - 2*i in dict.keys():
            print(i)
            result.append(i)
    else:
        return result
    
    return result

nums = [3,-4,5,-6,7,8,-10]

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
