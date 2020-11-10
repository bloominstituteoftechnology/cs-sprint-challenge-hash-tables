
def finder(files, queries):
    storage = {}
    result =  []
    
    for f in files:
                                    #! get the path to the file
        file_name = f.split("/")[-1]
        if file_name in storage:
                                    #! add or append the file path
            storage[file_name].append(f)
                                    #! else, leave the file path where it is
        else:
            storage[file_name] = [f]
    
                                    #! for each item in queries,
    for q in queries:
                                    #! if that item is in the bucket/slot,
        if q in storage:
                                    #! then at that item to the result
            result += storage[q]
    
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
