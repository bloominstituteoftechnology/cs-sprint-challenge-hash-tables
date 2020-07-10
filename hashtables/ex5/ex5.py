# Your code here


def finder(files, queries):
    # everything is provided so im not going to need blob or os or os.path
    # this looks like a simple string operation to comparison.
    # making the file paths into a flattend list of elements without path seps
    result = []
    files = flatten([x.split('/') for x in files])
    for i in queries:
        if i in files:
            result.append(i)
        else:
            pass
    return result


def flatten(l):
    """Takes a nth dimensional array `l` and makes it into a 1d array
    """
    return [y for x in l for y in x]


if __name__ == "__main__":
    files = ['/bin/foo', '/bin/bar', '/usr/bin/baz']
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
