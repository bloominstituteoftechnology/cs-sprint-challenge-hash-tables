# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    results = []
    for idx, file in enumerate(files): 
        file = file.split("/")
        for keyword in file:
            if keyword in dict: 
                dict[keyword].append(idx)
            else:
                dict[keyword]=[idx]
    for item in queries: 
        if item in dict: 
            if len(dict[item]) > 1:
                for n in dict[item]:
                    results.append(files[n])
            else:
                results.append(files[dict[item][0]])
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
