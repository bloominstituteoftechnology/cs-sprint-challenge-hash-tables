def finder(files, queries):
    """
    YOUR CODE HERE
    """
    
    dic = {}
    result = []

    for f in files:
        f_name = f.rsplit('/', 1)[1] 

        if f_name not in dic:
            dic[f_name] = []
        
        dic[f_name].append(f)

    for q in queries:
        if q in dic:
            result += dic[q]

    return result


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
