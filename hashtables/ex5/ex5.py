import os


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    table = {}
    for f in files:
        base = os.path.split(f)[-1]
        if base in table:
            table[base].append(f)
        else:
            table[base] = [f]
    result = []
    for q in queries:
        if q in table:
            result += table[q]

    return result


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
