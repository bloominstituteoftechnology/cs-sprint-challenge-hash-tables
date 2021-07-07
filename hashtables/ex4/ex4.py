def has_negatives(numbers):
    
    storage = set()
    result = []
    
    # for each element of array
    for n in numbers:
                                  #! find the negative value of numbers[n] 
        diff = 0 - n
                                  #! if absolute values are equal to positive numbers
        if diff in storage:
                                  #! store its absolute value in another vector
            result.append(abs(diff)) #! x = abs(-7.25) ---> 7.25
                                  #! else for each term in vector, print first its negative value and the positive value
        else:
                                  #! add the positive number with negative value in the array
            storage.add(n)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
