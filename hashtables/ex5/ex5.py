def finder(files, queries):

    file_dict = dict()

    for path in files:
        name = path.rpartition('/')[-1]
        if name not in file_dict:
            file_dict[name] = [path]
        else:
            file_dict[name].append(path)

    results = list()

    for query in queries:
        if query in file_dict:
            for path in file_dict[query]:
                results.append(path)

    return results


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
