# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create empty array
    result = []
    # loop over files strings
    for paths in range(len(files) - 1):
        print('!!!', paths)
    # loop over first querie index and see if it's "in" the file
        for query in range(len(queries) -1):
    # if so, add the entire file name
            if query in paths:
                        result[query]
    # if not, just ignore the query

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
