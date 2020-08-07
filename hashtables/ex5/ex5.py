# Your code here



def finder(files, queries):
    # Built in string method can seperate filnames from paths
    filenames = {}

    for name in files:
        filenames[name] = name.rsplit('/',1) [-1]

    # Initialize result
    result = []

    # Check queries against filenames
    for q in queries:
        result = result + [k for k, v in filenames.items() if v == q]


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
