# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # will make a dictionary that has the last part of the 
    # string path as the key and the value will be the 
    # full path this will be in a list.
    result = []
    my_paths = {}
    for file in files:
        # add each file in the files
        s = file.rpartition("/")
        s = s[-1]
        if s not in my_paths:
            my_paths[s] = []
        my_paths[s].append(file)

    # now will be going through the queries
    for q in queries:
        if q in my_paths:
            # will now loop through the list in the dictionary
            for theFile in my_paths[q]:
                # will append each file path to the  result
                result.append(theFile)

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
