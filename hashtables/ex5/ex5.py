def finder(files, queries):

    paths = {}

    for path in files:
        good_file_name = path.split('/')[-1]

        if good_file_name not in paths:
            paths[good_file_name] = [path]
        else:
            paths[good_file_name].append(path)

    result = []

    for query in queries:
        if query in paths:
            for path in paths[query]:
                result.append(path)

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
