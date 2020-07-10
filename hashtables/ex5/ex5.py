# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for file in files:
        parts = file.split("/")
        filename = parts[-1]

        if filename not in cache:
            cache[filename] = []
        cache[filename].append(file)

    for q in queries:
        if q in cache:
            result.extend(cache[q])

    return result


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
