# Your code here



def finder(files, queries):
    file_splits = {}
    result = []
    for file in files:
        split = file.split("/")
        if split[-1] not in file_splits:
            file_splits[split[-1]] = [file]
        else:
            file_splits[split[-1]].append(file)
    for query in queries:
        if query in file_splits:
            result.append(file_splits[query])
    result = [x for sl in result for x in sl]
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
