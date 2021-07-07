# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    f_table = {}
    q_table = {}

    for f in files:
        f_table[f] = None

    for q in queries:
        q_table[q] = None

    for key in f_table:
        filename = key.split("/")[-1]

        if filename in q_table:
            result.append(key)
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
