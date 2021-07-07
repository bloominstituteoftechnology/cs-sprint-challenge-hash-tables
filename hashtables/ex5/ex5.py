# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_names = {}
    result = []
    for path in files:
        split_path = path.split("/")
        file_name = split_path[-1]
        if file_name not in file_names:
            file_names.setdefault(file_name, [path])
        else:
            file_names[file_name].append(path)
        
    for query in queries:
        if query in file_names:
            for path in file_names[query]:
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
    