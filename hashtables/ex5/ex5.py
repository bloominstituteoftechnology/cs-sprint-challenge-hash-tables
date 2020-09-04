# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    dict = {}

    for item in files:
        x = item.rfind("/")
        x += 1
        q = item[x:]

        if q in dict:
            l = []

            x = dict[q]
            l.extend(x)
            l.append(item)
            
            dict[q] = l
        else:
            dict[q] = item
    
    l = []

    for item in queries:
        if item in dict:
            l.append(dict[item])


    return l


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
