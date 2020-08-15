# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # empty list
    result = []
    # empty htable for paths
    cache = {}

    # spliting the paths on '/', to get the key as the filename
    for x in files:
        key = x.rsplit('/', 1)[1] # use rsplit instead to begin splitting from right end of string, aka equivalent of .split('/')[-1]
        value = x

        # create new entry in htable if needed
        if key not in cache:
            cache[key] = []
        # add current path to cache (filename is key)
        cache[key].append(x)

    # for each filename in querie, checking to see if it is a key in the htable
    for y in queries:
        if y in cache:
            # if file found, add the path
            result += cache[y]

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
