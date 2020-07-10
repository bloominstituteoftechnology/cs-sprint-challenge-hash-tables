def has_negatives(a):
    result = []
    
    for i in a:
        if i <= 0:
            a.remove(i)
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
