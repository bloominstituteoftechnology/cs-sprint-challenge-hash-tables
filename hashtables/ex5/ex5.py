# Your code here

cache = {}

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for i, file in enumerate(files):
        if file not in cache:
            cache[file] = 1
    
    for q in queries:
        if q in cache:
            result.append(q)

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
