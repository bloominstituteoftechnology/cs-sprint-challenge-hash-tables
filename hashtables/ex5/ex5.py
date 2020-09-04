# Your code here

import os

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    map = {}
    for f in files:
        filename = os.path.basename(f)
        path = map.get(filename)
        if path is None:
            path = []
        path.append(f)
        map[filename] = path
    
    result = []
    for q in queries:
        pathlist = map.get(q)
        if pathlist is not None:
            result += pathlist
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
