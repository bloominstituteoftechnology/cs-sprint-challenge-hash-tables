# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    dir = dict()

    for file in files:
        parts = file.split("/")
        filename = parts[-1]
        if filename not in dir:
            dir[filename] = []
        dir[filename].append(file)
    
    for q in queries:
        if q in dir:
            result.extend(dir[q])
    
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
