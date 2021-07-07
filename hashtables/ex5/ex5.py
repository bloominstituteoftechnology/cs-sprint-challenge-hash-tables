
def finder(files, queries):
    cache = {}
    result = []

    for path in files:
        file_item = path.split('/')[-1]
        
        if file_item in cache:
            cache[file_item].append(path)
        else:
            cache[file_item] = [path]

    for q in queries:
        if q in cache:
            results = cache[q]
            for path in results:
                result.append(path)
        else:
            pass
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


# set up cache
# results list

# make a cache of paths
    # the file is the last name after last / divider
    # if item is in cache
        # append path to locations that are known
    #else
        # create a list if item is not in cache
    
    # loop to check queries
        # if query is in cache
            # set results to cache
            # return a list of paths
            # return lists into one list
                # append list of path
        # else pass
        
#return result