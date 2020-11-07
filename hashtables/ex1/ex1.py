'''
UPER

package has a weight limit and list of weights of item weights

function finds two items, whose sum of weights == weight limit

return (zero, one)
where each element represents the item weights of the two packages

the higher valued index should be placed in the zero'th index
smaller value should be placed in the first index.
if such a pair doesn't exist for the given inputs, it should return None.

should run in linear time.

e.g:
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

key = weight, value = index of weight.

dict = {
    4:0,
    6:1,
    10:2,
    15:3,
    16:4,
}

check if hashtable contains limit - weight, if yes, 
21 - 4 = does it contain 17? False
21 - 6 = 15 = true: index of 6 and index of 15 (which which is bigger num) and return
'''

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    #load dict with value and index
    our_dict = {}
    idx = 0
    for item in weights:
        if item in our_dict:
            pass
            print('passing')
        else:
            our_dict[item] = idx
            idx +=1

    print(f'dict: {our_dict}')
    #for each key in dict, 
    for item in our_dict:
        #limit - value
        print(f'item:{item}')
        check_weight = limit - item
        #check value exists
        if check_weight in our_dict:
            print(f'found! {check_weight}')
            if len(our_dict) == 1:
                return(1,0)
            if our_dict[item] < our_dict[check_weight]:
                print(our_dict[check_weight], our_dict[item])
                return(our_dict[check_weight], our_dict[item])
            else:
                print(our_dict[item], our_dict[check_weight])
                return(our_dict[item], our_dict[check_weight])
        
        #check which is bigger num
        #load index of bigger as zero'th
        #load index of small as first
        #return tuple


    return None

get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)