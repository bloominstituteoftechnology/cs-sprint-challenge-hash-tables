# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    files_found = []

    directory = {}

    for file in files:

        # keyName is last part of path
        parts = file.split("/")
        keyName = parts[-1]
        
        # create a new entry in the dictionary if needed
        if keyName not in directory:
            directory[keyName] = []
        
        # add current path to dictionary with the keyName as the key
        directory[keyName].append(file)

    # go through each query
    for query in queries:

        # if the file was found, add all the paths to the result to return
        if query in directory:
            files_found.append(directory[query])

    return files_found


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
