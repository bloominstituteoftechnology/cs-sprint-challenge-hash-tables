# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    files_dict = {}
    for each in files:
        
        each = each.split('/')
        
        key = each[-1]
        each = '/'.join(each)
        # handling collision
        if key in files_dict: 
            files_dict[key].append(each)
        else:
            files_dict[key] = [each]
    
    result = []    
    for each in queries:
        if each in files_dict:
            for file in files_dict[each]:    
                result.append(file)
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



    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")
    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")
    queries = []
    for i in range(1000000):
        queries.append(f"nofile{i}")
    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]
    result = finder(files, queries)
    result.sort()
    print(result)
    