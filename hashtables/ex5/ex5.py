# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for filename in queries:
        if filename not in cache:
            cache[filename] = filename
    
    for path in files:
        if "/" in path:
            filename = path.split("/")[-1]
            if filename in cache:
                result.append(path)

                

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
