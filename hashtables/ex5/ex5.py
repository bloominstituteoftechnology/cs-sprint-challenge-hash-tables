# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    file_hash = {}

    for q in queries:
        file_hash[q] = q

    for f in files:
        seperated = f.split('/')
        match = seperated[len(seperated) - 1]

        if match in file_hash:
            result.append(f)

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
