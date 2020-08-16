def has_negatives(a):
    num_dict = {}
    result = []
   
   
    for pos_num in a:
       num_dict[pos_num] = 1
       if pos_num != 0 and -pos_num in num_dict:
           result.append(abs(pos_num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
