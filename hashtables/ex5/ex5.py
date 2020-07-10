# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []

    file_directory = dict()

    for file in files:
        file_split = file.split("/")
        filename = file_split[-1]
        if filename not in file_directory:
            file_directory[filename] = []
        file_directory[filename].append(file)

    for query in queries:
        if query in file_directory:
            result.extend(file_directory[query])


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
