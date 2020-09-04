# Your code here


def finder(files, queries):
    # make a cache where the key value is the file name without the path
    cache = {k.split('/')[-1]: [] for k in files}
    result = []

    # loop over all of the paths that we have and save it to the key of the cache
    for f in files:
        f_type = f.split('/')[-1]
        cache[f_type].append(f)
    # check the quaries and see if they match a key in the cache if so then
    # return that full file path
    for q in queries:
        if q in cache:
            result += cache[q]

    return result


if __name__ == "__main__":
    files = ['/bin/foo', '/bin/bar', '/usr/bin/baz']
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
