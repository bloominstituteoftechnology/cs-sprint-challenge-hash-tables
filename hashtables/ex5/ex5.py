# Your code here
import ntpath

def finder(files, queries):

    cache = {}
    result = []
    
    for path in files:
        filename = ntpath.basename(path)
        if filename in cache:
            cache[filename].append(path)
        else:
            cache[filename] = path
    
    for filename in queries:
        if filename in cache:
            result.append(cache[filename])    
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