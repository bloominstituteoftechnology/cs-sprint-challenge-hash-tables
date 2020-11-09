num_dict = {}
numbers = 0
def intersection(arrays):
    first_round = True
    arraying = 0
    iteration = 0
    for array in arrays:
        arraying += 1
        iteration += 1
        for number in array:
            if first_round:
                if number in num_dict:
                    print("")
                else:
                    num_dict[number] = 1
            else:
                if number in num_dict:
                    if num_dict[number] + 1 == iteration:
                        num_dict[number] += 1
                    else:
                        # delete the number
                        del num_dict[number]
                        print("")
                else:
                    # delete the number
                    print("")
                    
        first_round = False
    
    for num in num_dict:
        print(num_dict[num])
        if num_dict[num] == iteration:
            print(num)
            return [num]
                    
    print(" - - -")
    



# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
