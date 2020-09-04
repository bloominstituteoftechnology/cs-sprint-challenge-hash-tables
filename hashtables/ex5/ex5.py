# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # result = []
    # seen = {}

    # for f in files:
    #     f.split('/')
    #     for queries in files:
    #         # for f in files:
    #         #     f.split('/')
    #         if queries in f:
    #             result.append(queries)
    #             seen[queries] = result
    # return result


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
