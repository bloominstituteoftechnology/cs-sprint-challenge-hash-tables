# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # get a cache where the last part is the key i.e a  path of /bin/foo would have the key foo
    cache = {k.split('/')[-1]: [] for k in files}
    result = []

    # loop over all the paths and append the full path to the key that matches it last part of the path
    for f in files:
        f_type = f.split('/')[-1]
        cache[f_type].append(f)

    # now we have a cache that has all possible last file paths and all paths that apply to that last part
    # loop thru our queries and if the query is in the cache then add the values of that key to our 
    # result list
    for q in queries:
        if q in cache:
            result += cache[q]

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
