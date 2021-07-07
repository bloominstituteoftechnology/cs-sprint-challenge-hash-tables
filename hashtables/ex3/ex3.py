def intersection(arrays):
   int_dict = {}
   
   for list in arrays:
       for item in list:
           if item in int_dict:
               int_dict[item]+= 1
           else:
               int_dict[item] = 1
    
   result = [item[0] for item in int_dict.items() if item[1] == len(arrays)]

   return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
