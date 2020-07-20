# Create a cache
cache = {}


def finder(files, queries):
    # Create a results arr
    res = []

    # Traverse the files, and build the cache
    for _, path in enumerate(files):
        # Get the filename by splitting the path on / and taking the last element
        filename = path.split("/")[-1]
        # If the filename is not in the cache, add a key of filename with a list containing the path to the cache
        if filename not in cache:
            cache[filename] = [path]
        # If key exists, append the list with the new path
        else:
            cache[filename].append(path)
    # Traverse the queries, trying to match the query to the keys in the cache
    for query in queries:
        # If found, add paths located in that key ot the results arr
        if query in cache:
            for path in cache[query]:
                res.append(path)

    return res


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
