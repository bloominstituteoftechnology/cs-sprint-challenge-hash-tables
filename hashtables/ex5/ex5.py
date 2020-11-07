# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_list = []
    my_dict = {}

    for v in files:
        f_name = v.split("/")[-1]
        
        if f_name in my_dict:
            my_dict[f_name].append(v)
        else:
            my_dict[f_name] = [v]
    
    for q in queries:
        if q in my_dict:
            my_list.extend(my_dict[q])
    
    return my_list


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        'usr/foo/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
