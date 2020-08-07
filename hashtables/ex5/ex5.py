
def finder(files, queries):

    cache = {}
    temp_result = []

    for url in files:
        # use split to get file name.
        file_name = url.split("/")[-1]

        if file_name in cache:
            cache[file_name] += "," + url
        else:
            cache[file_name] = url

    for query in queries:
        if query in cache:
            temp_result.append(cache[query])

    
    result = []
    
    for item in temp_result:
        for new_item in item.split(","):
            result.append(new_item)

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
