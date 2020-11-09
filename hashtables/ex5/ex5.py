# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    result = []
    for i in files:
        key = i.rsplit('/', 1)[-1]
        if key in dictionary:
            dictionary[key].append(i)
        else:
            dictionary[key] = [i]
    # print(dictionary)

    for i in queries:
        if i in dictionary:
            result = result + dictionary[i]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/shin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "bar"
    ]
    print(finder(files, queries))
