# Given a list of full paths to files, and a list of filenames to query, 
# report all the full paths that match that filename.
#
# Return list can be in any order.

def finder(files, queries):
    """
    files input is array of paths
    queries is list of filenames to query
    """
    # empty list
    result = []
    # empty ht for paths
    cache = {}

    # we can split the paths on '/', to get the key as the filename
    for x in files:
        key = x.rsplit('/', 1)[1] # can use rsplit instead to begin splitting from right end of string, aka equivalent of .split('/')[-1]
        value = x

        # create new entry in ht if needed
        if key not in cache:
            cache[key] = []
        # add current path to cache (filename is the key)
        cache[key].append(x)

    # for each filename in queries, check to see if it is a key in the ht
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
