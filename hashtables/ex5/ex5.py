# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # construct a dictionary where the index begins with the filename. then perform 
    # a search based on queries
    file_dict = {}
    for i in files:
        index = i[i.rfind('/')+1:]
        if index not in file_dict:
            file_dict[index] = [i]
        else:
            file_dict[index].append(i)


    output = []
    for i in queries:
        if i in file_dict:
            for j in file_dict[i]:
                output.append(j)

    return output


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
