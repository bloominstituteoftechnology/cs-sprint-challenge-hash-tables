# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []

    dictionary = dict()

    for file in files:

        component = file.split("/")
        filename = component[-1]

        if filename not in dictionary:
            dictionary[filename] = file
        
    for i in queries:
        if i in dictionary:
            result.append(dictionary[i])

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
